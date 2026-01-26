# sudo apt install libsndfile1
# pip install omnilingual-asr

from omnilingual_asr.models.inference.pipeline import ASRInferencePipeline

pipeline = ASRInferencePipeline(model_card="omniASR_LLM_3B")

audio_files = ["./audio/Lai.mp3", "./audio/Trump.mp3"]
lang = ["cmn_Hant", "eng_Latn"]
transcriptions = pipeline.transcribe(audio_files, lang=lang, batch_size=2)
print(transcriptions)
