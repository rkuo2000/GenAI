from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def home():
    html_content = """
    <html>
        <head><meta charset="utf-8" /></head>
        <body>
            <h1>This is a direct HTML response</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/asr")
async def asr():
    html_content = """

    <html>
    <head><meta charset="utf-8" /></head>
    <body>
    <script type="text/javascript">
    var infoBox; // 訊息 label
    var textBox; // 最終的辨識訊息 text input
    var tempBox; // 中間的辨識訊息 text input
    var startStopButton; // 「辨識/停止」按鈕
    var final_transcript = ''; // 最終的辨識訊息的變數
    var recognizing = false; // 是否辨識中

    function startButton(event) {
      infoBox = document.getElementById("infoBox"); // 取得訊息控制項 infoBox
      textBox = document.getElementById("textBox"); // 取得最終的辨識訊息控制項 textBox
      tempBox = document.getElementById("tempBox"); // 取得中間的辨識訊息控制項 tempBox
      startStopButton = document.getElementById("startStopButton"); // 取得「辨識/停止」這個按鈕控制項
      langCombo = document.getElementById("langCombo"); // 取得「辨識語言」這個選擇控制項
      if (recognizing) { // 如果正在辨識，則停止。
        recognition.stop();
      } else { // 否則就開始辨識
        textBox.value = ''; // 清除最終的辨識訊息
        tempBox.value = ''; // 清除中間的辨識訊息
        final_transcript = ''; // 最終的辨識訊息變數
        recognition.lang = langCombo.value; // 設定辨識語言
        recognition.start(); // 開始辨識
      }
    }

    if (!('webkitSpeechRecognition' in window)) {  // 如果找不到 window.webkitSpeechRecognition 這個屬性
      // 就是不支援語音辨識，要求使用者更新瀏覽器。 
      infoBox.innerText = "本瀏覽器不支援語音辨識，請更換瀏覽器！(Chrome 25 版以上才支援語音辨識)";
    } else {
      var recognition = new webkitSpeechRecognition(); // 建立語音辨識物件 webkitSpeechRecognition
      recognition.continuous = true; // 設定連續辨識模式
      recognition.interimResults = true; // 設定輸出中先結果。

      recognition.onstart = function() { // 開始辨識
        recognizing = true; // 設定為辨識中
        startStopButton.value = "按此停止"; // 辨識中...按鈕改為「按此停止」。  
        infoBox.innerText = "辨識中...";  // 顯示訊息為「辨識中」...
      };

      recognition.onend = function() { // 辨識完成
        recognizing = false; // 設定為「非辨識中」
        startStopButton.value = "開始辨識";  // 辨識完成...按鈕改為「開始辨識」。
        infoBox.innerText = ""; // 不顯示訊息
      };

      recognition.onresult = function(event) { // 辨識有任何結果時
        var interim_transcript = ''; // 中間結果
        for (var i = event.resultIndex; i < event.results.length; ++i) { // 對於每一個辨識結果
          if (event.results[i].isFinal) { // 如果是最終結果
            final_transcript += event.results[i][0].transcript; // 將其加入最終結果中
          } else { // 否則
            interim_transcript += event.results[i][0].transcript; // 將其加入中間結果中
          }
        }
        if (final_transcript.trim().length > 0) // 如果有最終辨識文字
            textBox.value = final_transcript; // 顯示最終辨識文字
        if (interim_transcript.trim().length > 0) // 如果有中間辨識文字
            tempBox.value = interim_transcript; // 顯示中間辨識文字
      };
    }
    </script>   
    <BR/>
    最後結果：<input id="textBox" type="text" size="60" value=""/><BR/>
    中間結果：<input id="tempBox" type="text" size="60" value=""/><BR/>
    辨識語言：
    <select id="langCombo">
      <option value="cmn-Hant-TW">中文(台灣)</option>
      <option value="en-US">英文(美國)</option>
    </select>
    <input id="startStopButton" type="button" value="語音辨識" onclick="startButton(event)"/><BR/>
    <label id="infoBox"></label>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
