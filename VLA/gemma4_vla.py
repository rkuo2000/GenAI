#!/usr/bin/env python3
"""Gemma 4 VLA Demo — press SPACE to talk, Gemma decides if it needs to look."""

import base64, json, os, select, signal, subprocess, sys, termios, textwrap
import threading, time, tty, urllib.request, wave, warnings

# Silence noisy warnings from ONNX Runtime and HuggingFace
os.environ["ORT_LOG_LEVEL"] = "3"
os.environ["ONNXRUNTIME_LOG_SEVERITY_LEVEL"] = "4"
os.environ["HF_HUB_VERBOSITY"] = "error"
warnings.filterwarnings("ignore")
sys.stderr = open(os.devnull, "w")

# ── Config (override with env vars before launching) ──────────────────────────

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/v1/chat/completions")
MIC       = os.getenv("MIC_DEVICE", "plughw:3,0")
SPK       = os.getenv("SPK_DEVICE", "alsa_output.usb-Generic_USB2.0_Device_20130100ph0-00.analog-stereo")
WEBCAM    = int(os.getenv("WEBCAM", "0"))
VOICE     = os.getenv("VOICE", "af_jessica")
AUDIO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio_prompts")
BGM_PATH  = os.path.join(AUDIO_DIR, "bgm.wav")

# PulseAudio volume levels (0–65536): normal voice, background music, ducked music
VOL_VOICE, VOL_BGM, VOL_DUCK = "39321", "32768", "6553"

# Terminal colors
CY, BL, DM, MG, GR, YL, WH, BD, R = (
    "\033[96m", "\033[94m", "\033[90m", "\033[95m",
    "\033[92m", "\033[93m", "\033[97m", "\033[1m", "\033[0m")

# ── Personality and tool: Gemma has one tool — the webcam ─────────────────────

SYSTEM = (
    "You are a helpful assistant on a Jetson Orin Nano Super with a webcam. "
    "If the user asks about something physical or visual, call look_and_answer. "
    "Otherwise answer directly. Keep it brief (1-3 sentences). Match the user's language.")

TOOLS = [{"type": "function", "function": {
    "name": "look_and_answer",
    "description": "Take a photo with the webcam and analyze what is visible.",
    "parameters": {"type": "object", "properties": {
        "question": {"type": "string", "description": "What to look for."}
    }, "required": ["question"]}
}}]

# Pre-generated voice prompts — cached as WAVs so she can speak instantly
PROMPTS = {
    "hello":                "Hello, I am Gemma Four. I run on a tiny Jetson Orin Nano Super.",
    "capturing_analyzing":  "Capturing and analyzing image.",
    "understanding":        "I'm understanding what I saw.",
}

# ── Audio: PulseAudio playback + background music ────────────────────────────

stt, tts, cam = None, None, None
bgm_proc, bgm_sink, bgm_on = None, None, False

def play_wav(path, vol=VOL_VOICE, wait=True):
    cmd = ["paplay", f"--device={SPK}", f"--volume={vol}", path]
    if wait: subprocess.run(cmd, capture_output=True, timeout=60)
    else:    return subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def bgm_vol(vol):
    if bgm_sink:
        try: subprocess.run(["pactl", "set-sink-input-volume", bgm_sink, str(vol)], capture_output=True, timeout=2)
        except: pass

def bgm_start():
    global bgm_proc, bgm_sink, bgm_on
    bgm_kill()
    if not os.path.exists(BGM_PATH): return
    bgm_on = True
    def loop():
        global bgm_proc, bgm_sink
        while bgm_on:
            if bgm_proc is None or bgm_proc.poll() is not None:
                bgm_proc = play_wav(BGM_PATH, vol=VOL_BGM, wait=False)
                time.sleep(0.2)
                try:
                    out = subprocess.check_output(["pactl", "list", "short", "sink-inputs"], text=True, timeout=2)
                    for ln in out.strip().split("\n"):
                        parts = ln.split()
                        if len(parts) >= 2: bgm_sink = parts[0]
                except: bgm_sink = None
            time.sleep(0.5)
    threading.Thread(target=loop, daemon=True).start()

def bgm_kill():
    global bgm_on, bgm_proc, bgm_sink
    bgm_on = False
    if bgm_proc and bgm_proc.poll() is None: bgm_proc.kill(); bgm_proc.wait()
    bgm_proc, bgm_sink = None, None

def play_prompt(name):
    path = os.path.join(AUDIO_DIR, f"{name}.wav")
    if not os.path.exists(path): return
    bgm_vol(VOL_DUCK)
    play_wav(path, wait=True)
    bgm_vol(VOL_BGM)

def speak(text):
    import soundfile
    pcm, sr = tts.create(text[:500], voice=VOICE, speed=1.1)
    soundfile.write("/tmp/vla_tts.wav", pcm, sr)
    bgm_vol(VOL_DUCK)
    play_wav("/tmp/vla_tts.wav", wait=True)
    bgm_vol(VOL_BGM)

# ── Load STT + TTS + webcam (runs once at startup) ───────────────────────────

def load_all():
    global stt, tts, cam
    import onnx_asr, kokoro_onnx, cv2
    from huggingface_hub import hf_hub_download

    def status(msg, step, total=4):
        sys.stdout.write(f"\r  {DM}[{'█'*step + '░'*(total-step)}] {msg}{R}    ")
        sys.stdout.flush()

    # Parakeet STT — 0.6B params, runs on CPU
    status("Loading STT engine...", 1)
    stt = onnx_asr.load_model("nemo-parakeet-tdt-0.6b-v3")

    # Kokoro TTS — 82M params, runs on CPU
    status("Loading TTS engine...", 2)
    m = hf_hub_download("fastrtc/kokoro-onnx", "kokoro-v1.0.onnx")
    v = hf_hub_download("fastrtc/kokoro-onnx", "voices-v1.0.bin")
    tts = kokoro_onnx.Kokoro(m, v)

    # Generate voice prompts (only re-generated if voice or text changes)
    status("Generating prompts...", 3)
    os.makedirs(AUDIO_DIR, exist_ok=True)
    meta_path = os.path.join(AUDIO_DIR, "meta.json")
    wanted = {"voice": VOICE, "prompts": PROMPTS}
    current = {}
    try:
        with open(meta_path) as f: current = json.load(f)
    except: pass
    if current != wanted:
        import soundfile
        for name, txt in PROMPTS.items():
            pcm, sr = tts.create(txt, voice=VOICE, speed=1.1)
            soundfile.write(os.path.join(AUDIO_DIR, f"{name}.wav"), pcm, sr)
        with open(meta_path, "w") as f: json.dump(wanted, f)

    # Open webcam and flush a few frames to warm it up
    status("Warming up webcam...", 4)
    subprocess.run(["fuser", "-k", f"/dev/video{WEBCAM}"], capture_output=True)
    time.sleep(0.3)
    cam = cv2.VideoCapture(WEBCAM)
    if not cam.isOpened(): time.sleep(1); cam = cv2.VideoCapture(WEBCAM)
    cam.set(3, 640); cam.set(4, 480)
    for _ in range(5): cam.read()
    status("Ready!", 4); print()

# ── Recording: SPACE → talk → SPACE ──────────────────────────────────────────

def record():
    print(f"\n  {DM}Press SPACE to start recording, SPACE again to stop.{R}\n")
    old = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        # Wait for first SPACE
        while True:
            ch = sys.stdin.read(1)
            if ch == "\x03": raise KeyboardInterrupt
            if ch == " ": break
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
        bgm_vol(VOL_DUCK)
        for p in ("/tmp/vla.pcm", "/tmp/vla.wav"):
            if os.path.exists(p): os.remove(p)

        # Start recording raw PCM from the microphone
        proc = subprocess.Popen(
            ["arecord", "-D", MIC, "-t", "raw", "-f", "S16_LE", "-r", "16000", "-c", "1", "/tmp/vla.pcm"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        t0 = time.time()
        print(f"  {MG}● REC  {DM}(press SPACE to stop){R}        ", end="\r", flush=True)

        # Wait for second SPACE
        while True:
            rdy, _, _ = select.select([sys.stdin], [], [], 0.1)
            if not rdy: continue
            ch = sys.stdin.read(1)
            if ch == "\x03": raise KeyboardInterrupt
            if ch == " ": break
        if proc.poll() is None: proc.send_signal(signal.SIGINT)
        try: proc.wait(timeout=3)
        except: proc.kill(); proc.wait()

        dur = time.time() - t0
        print(" " * 60, end="\r")
        if dur < 0.3 or not os.path.exists("/tmp/vla.pcm") or os.path.getsize("/tmp/vla.pcm") < 1024:
            print(f"  {DM}Too short — try again{R}"); return False

        # Convert raw PCM → WAV so Parakeet can read it
        raw = open("/tmp/vla.pcm", "rb").read()
        with wave.open("/tmp/vla.wav", "wb") as wf:
            wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(16000); wf.writeframes(raw)
        print(f"  {DM}Recorded {dur:.1f}s{R}"); return True
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old)

def transcribe():
    if not os.path.exists("/tmp/vla.wav") or os.path.getsize("/tmp/vla.wav") < 1024: return ""
    return (stt.recognize("/tmp/vla.wav") or "").strip()

# ── Webcam capture ────────────────────────────────────────────────────────────

def take_photo():
    global cam
    import cv2
    for _ in range(10): cam.grab()
    ok, frame = cam.read()
    if not ok:
        cam.release(); cam = cv2.VideoCapture(WEBCAM)
        cam.set(3, 640); cam.set(4, 480)
        for _ in range(5): cam.read()
        ok, frame = cam.read()
    if not ok: return None
    _, buf = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
    return base64.b64encode(buf).decode()

# ── LLM call to llama-server ──────────────────────────────────────────────────

def llm(messages, tools=None):
    body = {"model": "gemma4", "messages": messages, "max_tokens": 500,
            "temperature": 0.4, "thinking": {"type": "disabled"}}
    if tools: body["tools"] = tools
    req = urllib.request.Request(OLLAMA_URL, json.dumps(body).encode(), {"Content-Type": "application/json"})
    resp = json.loads(urllib.request.urlopen(req, timeout=120).read())
    msg = resp["choices"][0]["message"]
    msg["content"] = msg.get("content") or msg.get("reasoning_content") or ""
    return msg, resp.get("timings", {}).get("predicted_per_second", 0)

# ── The agent: Gemma decides if she needs to look or just answer ──────────────

def agent(question):
    print(f"  {MG}Thinking...{R}")
    if not bgm_on: bgm_start()
    else: bgm_vol(VOL_BGM)

    # First call — Gemma sees the question and the tool definition
    msg, tps = llm(
        [{"role": "system", "content": SYSTEM}, {"role": "user", "content": question}],
        tools=TOOLS)

    # No tool call → she already has the answer
    if not msg.get("tool_calls"):
        print(f"  {DM}Done — {tps:.0f} tok/s{R}")
        return msg["content"].strip()

    # She called look_and_answer → grab the webcam
    q = json.loads(msg["tool_calls"][0]["function"].get("arguments", "{}")).get("question", "Describe what you see.")
    print(f"  {CY}Gemma decided to LOOK!{R}")
    play_prompt("capturing_analyzing")
    bgm_vol(VOL_BGM)
    print(f"  {MG}Capturing + analyzing...{R}")

    img = take_photo()
    if not img: return "Could not capture from webcam."

    # Second call — Gemma sees the image and answers the visual question
    vis, _ = llm([{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img}"}},
        {"type": "text", "text": q + " Answer in 1-3 short sentences."}]}])
    print(f"  {DM}Done{R}")
    return vis["content"].strip()

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    text_mode = "--text" in sys.argv
    W = 62

    print(f"\n  {BL}{'▄' * W}{R}")
    print(f"""
{BD}{CY}   ██████  ███████ ███    ███ ███    ███  █████      ██   ██
  ██       ██      ████  ████ ████  ████ ██   ██     ██   ██
  ██   ███ █████   ██ ████ ██ ██ ████ ██ ███████     ███████
  ██    ██ ██      ██  ██  ██ ██  ██  ██ ██   ██          ██
   ██████  ███████ ██      ██ ██      ██ ██   ██          ██{R}
""")
    print(f"  {YL}{'Jetson Orin Nano Super · 100% Local · 2.3B params':^{W}}{R}")
    print(f"  {BL}{'▀' * W}{R}\n")

    if not text_mode:
        t0 = time.time()
        load_all()
        ln = "─" * W
        print(f"  {DM}{ln}{R}")
        print(f"  {DM}STT: Parakeet 0.6B · TTS: Kokoro 82M · LLM: Gemma 4 E2B · {time.time()-t0:.0f}s{R}")
        print(f"  {DM}{ln}{R}\n")
        play_prompt("hello")
        print(f"  {CY}{BD}[ SPACE ]{R} {DM}Talk to Gemma   {CY}{BD}[ Ctrl+C ]{R} {DM}Quit{R}\n")
    else:
        print(f"  {DM}Text mode — type a question, press Enter.{R}\n")

    while True:
        try:
            if text_mode:
                q = input(f"\n{CY}>{R} ").strip()
                if not q: continue
            else:
                if not record(): continue
                print(f"  {DM}Transcribing...{R}")
                q = transcribe()
                if not q: print(f"  {DM}Nothing detected.{R}\n"); bgm_vol(VOL_BGM); continue
                print(f"  {BL}{BD}You:{R} {WH}{q}{R}\n")

            answer = agent(q)
            print(f"\n  {BL}{'─' * W}{R}")
            for line in textwrap.wrap(answer, width=W - 4):
                print(f"  {GR}{BD}  {line}{R}")
            print(f"  {BL}{'─' * W}{R}\n")

            if not text_mode:
                speak(answer)
                print()
        except (KeyboardInterrupt, EOFError):
            bgm_kill()
            print(f"\n\n  {CY}Bye!{R}\n")
            break

if __name__ == "__main__":
    main()
