# 影視級 AI 微電影與短片全流程架構師 (Cinematic Micro-Movie Architect)

> **Cinematic Micro-Movie Architect** 是專為 **Antigravity / Claude Code / Cursor / Codex** 設計的影視工業級雙軌全流程 AI 短片生成技能。  
> 從故事概念、60 秒電影級分鏡劇本規劃、高解析關鍵影格生成、神經網路史詩評書旁白配音 (edge-tts)、純數學程序化戰鼓配樂與立體聲音效合成，到 FFmpeg 1080p 電影運鏡 (Ken Burns/Dolly/Pan) 與金邊字幕燒錄，一鍵全自動在本地合成 1080p MP4 短片成品；並同時產出外部 AI 視訊大模型（可靈 Kling、Runway Gen-3、海螺 MiniMax、Luma）專用之雙軌提示詞與參數手冊。

---

## 📌 核心架構與雙軌交付 (Dual-Track Pipeline)

```
使用者輸入主題 / 故事概念
        │
        ▼
[階段 1] 60 秒電影級分鏡劇本規劃（黃金三幕式 / 4~8 鏡頭切分 / 視聽對齊）
        │
        ▼
[階段 2] 關鍵影格 AI 生圖（Image 2.5 / Imagen 3 / FLUX / Midjourney / 16:9 電影構圖）
        │
        ▼
[階段 3] 神經網路旁白配音（edge-tts 史詩評書 / 沉穩歷史男聲 / 精確時長量測）
        │
        ▼
[階段 4] 程序化影視配樂與音效（Python wave/math 戰鼓轟鳴 / Sub-Bass 震盪 / 銅鑼鐘磬餘音）
        │
        ▼
[階段 5] FFmpeg 電影級運鏡合成與字幕燒錄（Ken Burns 動態 / ASS 金邊字幕 / 1080p MP4）
        │
        ├─────────────────────────────────────────┐
        ▼                                         ▼
【軌道一：本地即時播放 1080p MP4 成品】   【軌道二：外部 AI 視訊平台專用手冊】
- 50~60 秒 1080p 25/30fps MP4              - 可靈 Kling / Runway / 海螺 / Luma
- 內嵌旁白 + 戰鼓配樂 + 電影運鏡 + 燒錄字幕 - 各鏡頭中英 Motion Prompt + 相機代碼
- 存檔於專案目錄與桌面，立即可播            - 一鍵對齊預混主音軌 (master_audio.wav)
```

---

## 🚀 跨電腦快速安裝指引 (How to Install on Another Machine)

若要在另一台電腦上安裝並啟用本技能，請依作業系統執行以下一鍵指令：

### 🔹 方式一：Windows 環境（Antigravity / Gemini CLI）

開啟 **PowerShell**，執行以下命令自動克隆至 Antigravity 技能目錄：

```powershell
# 1. 建立技能目錄並 Clone
$skillDir = "$env:USERPROFILE\.gemini\config\skills\cinematic-micro-movie-architect"
if (-not (Test-Path $skillDir)) {
    git clone https://github.com/JeffreyHo0520/cinematic-micro-movie-architect.git $skillDir
} else {
    git -C $skillDir pull
}

# 2. 安裝 Python 相依套件
pip install edge-tts pillow

# 3. 確保 FFmpeg 可用（若尚未安裝可用 winget 安裝）
# winget install Gyan.FFmpeg
```

> **Claude Code 使用者安裝路徑**：
> 若您使用 Claude Code，可將 repo clone 至 `~/.claude/skills/cinematic-micro-movie-architect` 或專案目錄下的 `.claude/skills/`。

---

### 🔹 方式二：macOS / Linux 環境

開啟 **Terminal**，執行：

```bash
# 1. 建立技能目錄並 Clone
SKILL_DIR="$HOME/.gemini/config/skills/cinematic-micro-movie-architect"
mkdir -p "$(dirname "$SKILL_DIR")"
if [ ! -d "$SKILL_DIR" ]; then
    git clone https://github.com/JeffreyHo0520/cinematic-micro-movie-architect.git "$SKILL_DIR"
else
    git -C "$SKILL_DIR" pull
fi

# 2. 安裝 Python 相依套件
pip install edge-tts pillow

# 3. 確保 ffmpeg 已安裝
# macOS: brew install ffmpeg
# Ubuntu/Debian: sudo apt update && sudo apt install -y ffmpeg
```

---

### 🔹 方式三：使用專案內建的一鍵安裝腳本

若已將本 repo 下載至本地：

* **Windows**:
  ```powershell
  powershell -ExecutionPolicy Bypass -File .\install.ps1
  ```
* **macOS / Linux**:
  ```bash
  chmod +x ./install.sh && ./install.sh
  ```

---

## 🎬 觸發情境與使用方式

在對話中提及以下關鍵字即可自動呼叫本技能：

* `/cinematic-micro-movie-architect 主題：...`
* 「幫我製作一個 60 秒電影短片」
* 「生成三國割鬚棄袍微電影」
* 「端到端生成 AI 短片與配樂」
* 「製作 AI 影片分鏡、配音與外部 Kling / Runway 提示詞」

### 指令範例：

```text
/cinematic-micro-movie-architect 主題是割鬚棄袍：西涼精兵攻破潼關，大敗曹軍。亂軍之中西涼兵大喊：「穿紅袍的是曹操！」曹操嚇得趕緊脫掉紅袍；隨後兵馬又喊：「有鬍子的是曹操！」曹操驚慌之下連忙用佩劍割斷鬍鬚；最後又有人喊：「短鬍子的是曹操！」曹操只好扯下旗角包住脖子狼狽逃竄。馬超差一點就能一槍刺死曹操。
```

---

## 🛠️ 前置需求與依賴

| 工具 / 套件 | 用途 | 安裝方式 |
| :--- | :--- | :--- |
| **Python 3.10+** | 執行配樂合成與流程自動化 | 官方安裝包或系統套件管理 |
| **FFmpeg** | 電影運鏡渲染、混音與 ASS 字幕燒錄 | `winget install Gyan.FFmpeg` / `brew install ffmpeg` |
| **edge-tts** | 微軟神經網路語音合成（旁白評書腔） | `pip install edge-tts` |
| **Pillow (PIL)** | 影像解析度調整與影格調色 | `pip install pillow` |

---

## 📁 專案生成目錄標準結構

執行技能後，將自動產出規範化之電影短片專案結構：

```text
[主題]_AI短片專案/
├── [主題]_60秒AI電影短片.mp4          ← 最終 1080p 電影短片成品
├── README_外部AI視訊生成指南.md       ← 外部 AI 視訊大模型專用提詞手冊
├── assets/
│   ├── scene_01.jpg ~ scene_06.jpg     ← 1080p 關鍵影格
│   ├── scene_01_voice.mp3 ...          ← 各鏡頭旁白語音檔
│   ├── cinematic_bgm.wav               ← 純數學程序化立體聲戰鼓配樂
│   ├── master_audio.wav                ← 混音完成之全片主音軌
│   ├── subtitles.ass                   ← 影視級微軟正黑體金邊字幕檔
│   └── scene_01_clip.mp4 ...           ← 帶 Ken Burns 運鏡之獨立鏡頭片段
└── scripts/
    └── build_full_movie.py             ← 全自動一鍵重構與渲染腳本
```

---

## 📄 開源授權

本專案採 [MIT License](LICENSE) 授權開源。
歡迎 Fork、Star 與貢獻！
