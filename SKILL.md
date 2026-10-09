---
name: cinematic-micro-movie-architect
description: >-
  影視級 AI 微電影與短片全流程架構師 (Cinematic Micro-Movie Architect)。
  從概念發想、60 秒電影級腳本拆解、高解析關鍵影格生圖 (generate_image/FLUX/MJ)、
  神經網路史詩旁白配音 (edge-tts)、程序化戰鼓配樂與立體聲音效合成、到 FFmpeg 電影運鏡 (Ken Burns/Dolly/Pan)
  與金邊字幕燒錄，一鍵全自動在本地合成 1080p MP4 短片成品；並同時產出外部 AI 視訊大模型（可靈 Kling、Runway Gen-3、海螺 MiniMax）
  專用之雙軌提示詞與參數手冊。當使用者提到「做 AI 短片」、「生成微電影」、「做 60 秒短片」、「影片腳本與生成影片」、「文字生成電影短片」、「端到端生成短片」時觸發。
---

# 影視級 AI 微電影與短片全流程架構師 (Cinematic Micro-Movie Architect)

## 📌 技能定位與核心價值

在現代短影音、歷史演義、遊戲預告與廣告企劃中，單純產出文字腳本或靜態圖像無法帶給使用者立即可感受的視聽震撼；而直接使用昂貴的外部 AI 視訊平台（如 Kling、Runway）又常面臨抽卡成本高、鏡頭間人物不一致、以及欠缺配樂旁白與字幕的痛點。

`cinematic-micro-movie-architect` 提供完整的**影視工業級雙軌全流程（Dual-Track Pipeline）**：

```
使用者輸入主題 / 需求
        │
        ▼
[階段 1] 60 秒電影級分鏡劇本規劃（黃金三幕式 / 4~8 鏡頭切分 / 視聽對齊）
        │
        ▼
[階段 2] 關鍵影格 AI 生圖（generate_image / 16:9 電影構圖 / 光影一致性）
        │
        ▼
[階段 3] 神經網路旁白配音（edge-tts 史詩評書 / 沉穩歷史男聲 / 精確時長量測）
        │
        ▼
[階段 4] 程序化影視配樂與音效（Python wave/math 戰鼓轟鳴 / 重低音 / 銅鑼餘音）
        │
        ▼
[階段 5] FFmpeg 電影級運鏡合成與字幕燒錄（Ken Burns 動態 / ASS 金邊字幕 / 1080p MP4）
        │
        ├─────────────────────────────────────────┐
        ▼                                         ▼
【軌道一：本地即時播放 MP4 成品】        【軌道二：外部 AI 視訊平台專用手冊】
- 50~60 秒 1080p 30fps MP4                - 可靈 Kling / Runway / 海螺 / Sora
- 內嵌旁白 + 戰鼓配樂 + 電影運鏡 + 燒錄字幕 - 各鏡頭中英 Motion Prompt + 相機代碼
- 存檔於專案目錄與桌面，立即可播          - 一鍵對齊預混音訊 (master_audio.wav)
```

---

## 🎬 標準工作流（6-Step Pipeline）

### 第一步：故事企劃與黃金時長分鏡規劃 (Story & Rhythm Planning)
1. **控制時長**：嚴格限制在 50~60 秒以內（符合 YouTube Shorts / Reels / TikTok 黃金完播率）。
2. **三幕式節奏切分**：
   - **開篇蓄勢（00:00 - 00:15）**：建立世界觀、危機逼近、主角受命或立誓。
   - **衝突激化（00:15 - 00:30）**：奔赴戰場、鐵騎狂馳、風沙漫卷、萬軍辟易。
   - **高潮爆發（00:30 - 00:45）**：斬將奪旗、神威凱旋、強烈對比（震撼全場）。
   - **定格餘韻（00:45 - 00:58）**：細節特寫（如溫酒猶熱、名刀入鞘）、留白與哲理收尾。
3. **分鏡表設計**：明確列出鏡號、時長、景別（EWS/MS/CU/Macro）、鏡頭運動（Zoom/Pan/Tilt）、視覺焦點與音效設計。

### 第二步：關鍵影格生圖 (Keyframe Generation)
1. 調用 `generate_image` 或外部模型產出 3~5 張代表性關鍵影格。
2. **提示詞工程標準**：
   - 比例：`16:9`（寬螢幕電影感）或 `9:16`（直式短影音）。
   - 光影控制：強烈要求 `golden hour sunset rim light`（金色逆光輪廓）、`chiaroscuro lighting`（明暗對比）。
   - 細節強化：`atmospheric dust`, `flying sand`, `8k resolution`, `dramatic film still`。
   - 人物與美術一致性：鎖定核心色彩（如關羽「綠袍金甲、長鬚美髯、赤兔馬、青龍偃月刀」）。

### 第三步：神經網路旁白配音 (Neural Voiceover via edge-tts)
1. 使用 Python 呼叫 `edge-tts` 自動生成高自然度廣播級語音。
2. **音色推薦清單**：
   - **史詩 / 歷史評書 / 戰場紀錄片**：`zh-CN-YunjianNeural`（沉穩雄渾、穿透力強，推薦 rate="-5%", pitch="-2Hz"）
   - **現代紀實 / 懸疑短片**：`zh-CN-YunxiNeural` 或 `zh-TW-YunJheNeural`
   - **女性知性旁白**：`zh-TW-HsiaoChenNeural` 或 `zh-CN-XiaoxiaoNeural`
3. 使用 `ffprobe` 自動讀取各音檔的精確秒數，動態反饋調整視訊剪輯長度。

### 第四步：程序化影視配樂與音效 (Procedural Soundscape & SFX)
1. 無需外掛付費音訊庫，利用 Python 純標準庫（`wave`, `struct`, `math`, `random`）動態合成無版權之立體聲電影音效：
   - **戰鼓打擊（War Drum）**：50~65Hz 低頻正弦波 + 指數衰減 + 破音雜訊瞬態。
   - **氛圍嗡鳴（Sub Bass Drone）**：55Hz (A1) + 82.4Hz (E2) + 110Hz (A2) 堆疊低頻震盪。
   - **金屬鐘磬 / 銅鑼餘音（Gong / Cymbal）**：320Hz~950Hz 多頻諧波集群 + 長尾衰減。
2. 根據分鏡節奏編排鼓點（開篇沉穩低鳴 ➔ 中段雙擊馬蹄節奏 ➔ 高潮前密集滾奏 ➔ 凱旋重音落地）。
3. 使用 FFmpeg `amix` 與 `adelay` 將旁白與配樂混合成 `master_audio.wav`。

### 第五步：FFmpeg 電影級運鏡合成與字幕燒錄 (FFmpeg Motion & Burnt Subtitles)
1. **Ken Burns 運鏡**：
   - 以 `zoompan` 濾鏡實現平滑微縮放與平移，消除靜態圖片的呆板感。
   - 縮放幅度控制在 `1.10 ~ 1.25` 之間，避免過度模糊。
2. **ASS 影視字幕規範**：
   - 字體：`Microsoft JhengHei`（微軟正黑體粗體）
   - 字級：`48 ~ 52px`（1080p 基準）
   - 顏色：主字白色（`&H00FFFFFF`）搭配 3px 深色描邊與陰影，保證在明暗背景均清晰可讀。
3. **一鍵導出**：產出 1920x1080 H.264 / AAC MP4 影片，儲存於工作目錄。

### 第六步：外部 AI 視訊手冊交付 (External Video Model Guide)
同步輸出 `README_外部AI視訊生成指南.md`，提供：
1. 各鏡頭在可靈 Kling / Runway / 海螺 AI 的上傳對應表。
2. 中英文雙語 Motion Prompt（精確描述動作、布料、馬匹、流體、表情微動）。
3. 相機控制代碼（Horizontal, Vertical, Zoom, Motion Strength 4~8）。
4. 剪映 / Premiere 時間軸一鍵對齊說明。

---

## 🛠️ 專案目錄結構規範

執行本技能時，應自動建立以下結構：

```
[主題]_AI短片專案/
├── [主題]_60秒AI電影短片.mp4          ← 最終 1080p 影片成品
├── README_外部AI視訊生成指南.md       ← 外部視訊大模型提詞手冊
├── assets/
│   ├── scene_01.jpg ~ scene_04.jpg     ← 高解析關鍵影格
│   ├── scene_01_voice.mp3 ...          ← 各鏡頭旁白語音
│   ├── cinematic_bgm.wav               ← 合成之史詩配樂
│   ├── master_audio.wav                ← 混音完成主音軌
│   ├── subtitles.ass                   ← 影視格式字幕檔
│   └── clip_01.mp4 ~ clip_04.mp4       ← 帶運鏡之個別場景片段
└── scripts/
    └── build_full_movie.py             ← 全自動重構與算圖腳本
```

---

## 💡 最佳實踐與防呆提示

1. **時長守則**：腳本總字數宜在 120 ~ 160 字之間（中文語速約每秒 3~3.5 字，預留 10~15 秒純音樂與音效呼吸空間）。
2. **文字編碼防呆**：Windows 環境下執行 FFmpeg 命令時，字幕檔案路徑需將反斜線 `\` 替換為正斜線 `/`，冒號轉義為 `\:`。
3. **生圖一致性**：每張圖的 Prompt 必須重複相同的核心特徵錨點（如：角色外觀、服飾材質、核心道具、天候光影）。
