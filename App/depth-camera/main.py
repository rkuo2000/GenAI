import cv2
import torch
import numpy as np
import os
import gradio as gr
from PIL import Image
import plotly.graph_objects as go

try:
    import spaces
except ImportError:
    pass

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

MODEL_CONFIGS = {
    "small": "depth-anything/Depth-Anything-V2-Small-hf",
    "base": "depth-anything/Depth-Anything-V2-Base-hf",
    "large": "depth-anything/Depth-Anything-V2-Large-hf",
}


class DepthAnythingPipeline:
    def __init__(self, model_name):
        self.model_name = model_name
        self.pipe = None

    def load(self):
        if self.pipe is None:
            from transformers import pipeline

            print(f"Loading model: {self.model_name}")
            self.pipe = pipeline(
                "depth-estimation",
                model=self.model_name,
                device=DEVICE,
            )
            print("Model loaded!")

    def infer(self, image):
        self.load()

        if isinstance(image, np.ndarray):
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        depth = self.pipe(image)["depth"]
        return np.array(depth)


depth_pipeline = None


def get_pipeline(model_name):
    global depth_pipeline
    if depth_pipeline is None or depth_pipeline.model_name != model_name:
        depth_pipeline = DepthAnythingPipeline(model_name)
    return depth_pipeline


def colorize_depth(depth):
    depth_min = depth.min()
    depth_max = depth.max()
    normalized = (depth - depth_min) / (depth_max - depth_min + 1e-8)
    normalized = (normalized * 255).astype(np.uint8)
    colored = cv2.applyColorMap(normalized, cv2.COLORMAP_INFERNO)
    return colored


def create_point_cloud_image(rgb_image, depth, max_points=20000):
    h, w = depth.shape
    rgb = cv2.resize(rgb_image, (w, h))

    cx = w / 2
    cy = h / 2
    fx = w / 2
    fy = w / 2

    points = []
    colors = []

    step = max(1, int(np.sqrt((h * w) / max_points)))

    for y in range(0, h, step):
        for x in range(0, w, step):
            z = depth[y, x]
            if z > 0:
                X = (cx - x) * z / fx
                Y = (y - cy) * z / fy
                points.append([X, Y, z])
                colors.append(rgb[y, x] / 255.0)

    if not points:
        return None

    points = np.array(points, dtype=np.float64)
    colors = np.array(colors, dtype=np.float64)

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=points[:, 0],
                y=points[:, 1],
                z=points[:, 2],
                mode="markers",
                marker=dict(size=2, color=colors, colorscale="Viridis"),
            )
        ],
        layout=go.Layout(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
            ),
            margin=dict(l=0, r=0, t=0, b=0),
            height=400,
        ),
    )

    return fig


def process_image(image, model_size):
    if image is None:
        return None, None, "Please upload an image"

    model_name = MODEL_CONFIGS[model_size]
    pipeline = get_pipeline(model_name)

    img = np.array(image)
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

    depth = pipeline.infer(img)
    colored = colorize_depth(depth)

    pcd_fig = create_point_cloud_image(img, depth)

    return colored, pcd_fig, f"Depth map generated successfully!"


class DepthAnythingApp:
    def __init__(self, model_name="depth-anything/Depth-Anything-V2-Small-hf"):
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = None
        self.running = True

        print(f"Using device: {self.device}")

    def load_model(self):
        from transformers import pipeline

        print(f"Loading {self.model_name} model...")
        self.pipe = pipeline(
            "depth-estimation", model=self.model_name, device=self.device
        )
        print("Model loaded successfully!")

    def infer_depth(self, image):
        if self.pipe is None:
            self.load_model()

        h, w = image.shape[:2]
        depth = self.pipe(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))[
            "depth"
        ]
        depth = np.array(depth)

        if depth.shape != (h, w):
            depth = cv2.resize(depth, (w, h))

        return depth

    def capture_webcam(self, camera_index=0):
        cap = cv2.VideoCapture(camera_index)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if not cap.isOpened():
            print("Error: Could not open webcam")
            return

        print("Webcam opened. Press 'q' to quit, 's' to save point cloud")

        vis_window = "Depth Camera"
        cv2.namedWindow(vis_window)

        while self.running:
            ret, frame = cap.read()
            if not ret:
                break

            depth = self.infer_depth(frame)
            colored_depth = self.colorize_depth(depth)

            combined = np.hstack([frame, colored_depth])
            cv2.imshow(vis_window, combined)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

    def colorize_depth(self, depth):
        depth_min = depth.min()
        depth_max = depth.max()
        normalized = (depth - depth_min) / (depth_max - depth_min + 1e-8)
        normalized = (normalized * 255).astype(np.uint8)
        colored = cv2.applyColorMap(normalized, cv2.COLORMAP_INFERNO)
        return colored

    def stop(self):
        self.running = False


def build_web_ui(port=7860, share=False):
    with gr.Blocks(title="Depth Anything V2") as app:
        gr.Markdown("# Depth Anything V2 - Web UI")
        gr.Markdown(
            "Upload an image or use webcam to generate depth map and 3D point cloud"
        )

        with gr.Row():
            with gr.Column():
                model_size = gr.Radio(
                    ["small", "base", "large"],
                    value="small",
                    label="Model Size",
                )
                gr.Markdown("### Upload Image or Capture from Webcam")
                image_input = gr.Image(
                    sources=["upload", "webcam", "clipboard"],
                    type="numpy",
                    label="Upload Image or Capture from Webcam",
                )
                process_btn = gr.Button("Generate Depth", variant="primary")

            with gr.Column():
                gr.Markdown("### Results")
                with gr.Row():
                    output_depth = gr.Image(label="Depth Map", value=None)
                    output_3d = gr.Plot(label="3D Point Cloud (Interactive)")

        with gr.Row():
            status_output = gr.Textbox(
                label="Status",
                interactive=False,
                show_label=False,
            )

        process_btn.click(
            fn=process_image,
            inputs=[image_input, model_size],
            outputs=[output_depth, output_3d, status_output],
        )

        gr.Markdown("---")
        gr.Markdown(
            "**Controls:** Upload image and click 'Generate Depth', or use webcam for real-time depth"
        )

        app.queue(max_size=2).launch(
            server_name="0.0.0.0",
            server_port=port,
            share=share,
        )


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Depth-Anything-V2 Web App")
    parser.add_argument(
        "--model",
        type=str,
        default="depth-anything/Depth-Anything-V2-Small-hf",
        help="Model name from HuggingFace",
    )
    parser.add_argument("--port", type=int, default=7860, help="Server port")
    parser.add_argument(
        "--share", action="store_true", help="Create public Gradio link"
    )

    args = parser.parse_args()

    print("Starting web UI with image upload and webcam support...")
    build_web_ui(port=args.port, share=args.share)


if __name__ == "__main__":
    main()
