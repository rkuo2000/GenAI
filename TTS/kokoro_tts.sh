# !pip install kokoro-tts
text = "Hello, this is a test of the Kokoro CLI engine."
# Basic text-to-speech output
kokoro-tts <text speech.wav

# Specify a specific voice and speed adjustment
#kokoro-tts "Reading text slightly faster." fast.mp3 --voice af_bella --speed 1.2

# Process an entire text document
#kokoro-tts manuscript.txt audiobook.wav
