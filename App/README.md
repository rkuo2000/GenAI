## HTTPS Server

1. 將AI產生的html (例如: ai_studio_code.html) 複製到 index.html
2. `python main.py`
3. 以電腦或手機打開Chrome瀏覽器，輸入`https://127.0.0.1:8000` 或 `https://192.168.0.14:8000` (192.168.0.14 是PC連網的位址）

## App生成之提示詞

### alphabet.html
```
寫出一個網頁給幼兒園學習26個英文字母，搭配單字，要能發出聲音與顯示圖片，要加上RWD
```

### alchemy.html
```
寫一個html 以國中化學為內容，產生一個小小煉金術師實驗室，可選擇化學基本元素及顯示其圖片，選定元素後進行合成或重置，並以web3D產生動畫，顯示最後之合成物的分子結構，及此合成物的圖片, 加上RWD, 合成鍋畫成一個古代爐鼎，無法合成時提示可合成之元素組成
```

### heartbeat.html
```
寫出一個html 使用webcam偵測人臉，利用rPPG演算法，感測出心跳BPM及顯示心跳波形, 加入band-pass filter, 加入RWD
```

### coco_ssd.html
```
寫一個html做物件辨識，輸入方式可選上傳照片或由webcam拍攝，選定輸入後要顯示其照片，按鍵進行辨識照片中的物件，最後顯示其物件的照片及其中英文名稱，提供重置鍵重新執行, 支援RWD
```

### image_poem.html
```
寫一個html作詩系統，輸入主題的方式可選上傳照片或由webcam拍攝，選定輸入按鍵後使用Gemini辨識（輸入Gemini API) 並作詩一首， 最後產生照片與詩句結合的圖片，支援RWD
```



