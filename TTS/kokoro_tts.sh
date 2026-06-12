# !pip install kokoro
# !pip install misaki[zh] # ja

kokoro -t "Hello, this is a test of the Kokoro CLI engine." -o output.mp3 --voice af_heart 

# Specify a specific voice and speed adjustment
kokoro -t "Reading text slightly faster." -o fast.mp3 --voice af_bella --speed 1.2

kokoro -t "很高興認識你" -o hello.mp3 -l z
