# pip install git+https://github.com/SYSTRAN/faster-whisper.git

from faster_whisper import WhisperModel

model = WhisperModel("large-v3", device="cuda", compute_type="float16")

inputfile = "audio1.flac"
#inputfile = "audio2.mp3"
#inputfile = "audio3.mp4"

segments, info = model.transcribe(inputfile, beam_size=5)

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
