# pip install googletrans==4.0.0rc1

from googletrans import Translator

translator = Translator()
result = translator.translate("一個很棒的沙發", dest="en").text
print(result)
