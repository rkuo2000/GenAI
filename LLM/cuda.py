import torch

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU name: {torch.cuda.get_device_name(0)}")
    print(f"CUDA version PyTorch was built with: {torch.version.cuda}")
    # Check supported architectures (sm_120 should be present in the output of a working build)
    print(f"Supported architectures: {torch.cuda.get_arch_list()}")

