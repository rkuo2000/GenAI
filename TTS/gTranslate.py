# pip install googletrans

import asyncio
from googletrans import Translator

async def translate_text():
    async with Translator() as translator:
        result = await translator.translate("一個很棒的沙發", dest="en")
        print(result.text)

asyncio.run(translate_text())
