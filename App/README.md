# Vibe Coding

---
## Coder

### [AntiGravity](https://antigravity.google/)

#### [Getting-Started](https://antigravity.google/docs/get-started)**
#### [Agent Modes / Settings](https://antigravity.google/docs/agent-modes-settings)**
  
**[Antigravity Vibe Coding 實戰工作坊](https://kevintsai1202.github.io/Antigravity_Course/)** <br>

**Antigravity 設定與應用：規則（Rules）＋神技能（Skills）＋自動化（Workflows）** <br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/e-WNdM4JO2U)](https://youtu.be/e-WNdM4JO2U)

---
### [Claud-code](https://github.com/anthropics/claude-code)
**Install**: `curl -fsSL https://claude.ai/install.sh | bash` <br>

![](https://github.com/anthropics/claude-code/raw/main/demo.gif)

---
### [OpenCode](https://github.com/anomalyco/opencode)
**Install**: `npm i -g opencode-ai@latest` <br>

![](https://github.com/anomalyco/opencode/raw/dev/packages/web/src/assets/lander/screenshot.png)

**OpenCode setup: Beginner’s Crash course** <br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/8toBNmRDO90)](https://youtu.be/8toBNmRDO90)

**OpenCode詳細攻略** <br>
[![](https://markdown-videos-api.jorgenkh.no/youtube/JYVTUU9ClUA)](https://youtu.be/JYVTUU9ClUA)

---
## App 範例

### HTTPS Server
1. 將AI產生的html (例如: ai_studio_code.html) 複製到 index.html
2. `python main.py`
3. 以電腦或手機打開Chrome瀏覽器，輸入`https://127.0.0.1:8000` 或 `https://192.168.0.14:8000` (192.168.0.14 是PC連網的位址）

---
### [alphabet.html](https://rkuo2000.github.io/app-alphabet/)
```
寫出一個網頁給幼兒園學習26個英文字母，搭配單字，要能發出聲音與顯示圖片，要加上RWD
```

### [alchemy.html](https://rkuo2000.github.io/app-alchemy/)
```
寫一個html 以國中化學為內容，產生一個小小煉金術師實驗室，可選擇化學基本元素及顯示其圖片，選定元素後進行合成或重置，並以web3D產生動畫，
顯示最後之合成物的分子結構，及此合成物的圖片, 加上RWD, 合成鍋畫成一個古代爐鼎，無法合成時提示可合成之元素組成
```

### [heartbeat.html](https://rkuo2000.github.io/app-heartbeat/)
```
寫出一個html 使用webcam偵測人臉，利用rPPG演算法，感測出心跳BPM及顯示心跳波形,
加入band-pass filter, 加入RWD
```

### [coco_ssd.html](https://rkuo2000.github.io/app-coco_ssd/)
```
寫一個html做物件辨識，輸入方式可選上傳照片或由webcam拍攝，選定輸入後要顯示其照片，按鍵進行辨識照片中的物件，
最後顯示其物件的照片及其中英文名稱，提供重置鍵重新執行, 支援RWD
```

### [image_poem.html](https://rkuo2000.github.io/app-image_poem/)
```
寫一個html 影像作詩系統，輸入主題的方式可選上傳照片或由webcam拍攝，選定輸入按鍵後使用Gemini辨識（輸入Gemini API) 並作詩一首，
最後產生照片與詩句結合的圖片，支援RWD
```

### [polePID_sim.html](https://rkuo2000.github.io/app-polePID_sim/)
```
我是一個電機系學生，請幫我寫一個單軸橫桿平衡的PID模擬網頁工具。
1. 物理模型：模擬一個中間有支點的長桿，兩端有馬達推力。系統輸入為PID參數。
2. 參數輸入項：PID 增益（Kp, Ki, Kd)
  * 系統去樣時間（預設 0.02s)
  * 橫桿重量與長度（模擬慣性）
3. 視覺與動畫：
  * 網頁上方顯示一個橫桿的簡易動畫，會根據當前角度傾斜。
  * 使用Chart.js同步繪製角度隨時間變化的響應曲線（類似MATLAB模擬圖）
4. 功能按鍵：
  *『開始模擬』：讓橫桿從傾斜30度開始，由PID回正。
  *『重置』：恢復初始狀態。
5. 介面要求：使用繁體中文，介面要乾淨現代化（使用Tailwindd CSS渲染）。所有代碼整合在一個html檔案中。
```

### [cmos_op.html](https://rkuo2000.github.io/app-cmos_op/)

### [排球AI分析系統](https://chenrays.github.io/AI_COURSE_Project_Present_Volleyball_Game_Analysis/)

### [Web3D全星空投像儀](https://anonymous-villager.github.io/Light_pollution/)

---
### [galaxian](https://rkuo2000.github.io/app-galaxian)
**Blog**: [Galaxian 遊戲指南與開發更新](https://vocus.cc/article/697f7388fd89780001b59a98)<br>

### opencode : `Kimi K2.5 Free`
```
開發一款經典街機遊戲《Galaxian》的網頁版克隆作品，並嚴格採用了 80 年代霓虹復古 (Neon Retro) 的美學風格。

1. 遊戲架構更新
index.html： 更新了使用者介面 (UI)，可即時顯示 等級 (Level)、護盾 (Shield) 與 生命值 (Lives) 狀態。
game.js： 全面重構，以支援等級晉升系統與玩家生命機制。
PWA 支援： 新增了 manifest.json，讓玩家可以將遊戲「新增至主畫面」。
音效系統： 內建程序化音效管理器 (SoundManager)。
2. 視覺進化（最終版）
像素藝術精靈圖： 採用道地的 8 位元 (8-bit) 像素風格繪製敵機與戰機。
星雲背景： 程序化生成的星雲雲團，增添了深邃的太空氛圍。
噴射尾跡： 玩家戰機在飛行時會釋放粒子尾跡。
擊中閃爍： 敵人被擊中時會閃爍白光，強化打擊感。
動態解析度： 完美適配各種螢幕尺寸。
行動裝置縮放： 針對手機螢幕優化了物件大小。
3. 遊戲機制（最終版）
敵人 AI（重新平衡）：
更公平的射擊： 降低了敵方火力密度。
垂直循環： 敵人會從頂部整齊地重新進入戰場。
自動置中： 敵人蜂群會自動保持在畫面中央。
行動版陣型： 在手機上將蜂群縮減至 6 欄，以防畫面過於雜亂。
積分紀錄： 本地端儲存前 10 名高分紀錄。
增益道具 (Power-Ups)：
❤️ 愛心： 恢復 1 點生命值。
🛡️ 護盾： 增加 2 次護盾充能。
⚡ 三連發： 武器升級（擴散彈）。
✈️ 僚機： 部署兩架側翼戰機協同作戰。
關卡： 共 50 個關卡，難度隨等級遞增。
4. 音效控制
音效 (SFX)： 雷射射擊、爆炸聲、道具取得鈴聲。
音樂： 復古低音 (Bassline) 背景音樂與過關鈴聲。
5. 操作方式
裝置移動射擊護盾PC 端方向鍵 或 滑鼠空白鍵 或 滑鼠左鍵滑鼠右鍵行動端觸控並拖曳螢幕任意位置觸碰螢幕時自動射擊快速連按三下 (0.75秒內)
```
![](https://github.com/rkuo2000/GenAI/blob/main/assets/App-galaxian.png?raw=true)

