#!/usr/bin/env bash
# Cinematic Micro-Movie Architect 一鍵安裝腳本 (macOS / Linux)

set -e

echo "=========================================================="
echo "🎬 正在安裝 Cinematic Micro-Movie Architect 技能 (macOS/Linux)..."
echo "=========================================================="

TARGET_DIR="$HOME/.gemini/config/skills/cinematic-micro-movie-architect"
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ "$CURRENT_DIR" != "$TARGET_DIR" ]; then
    echo "正在部署檔案至: $TARGET_DIR"
    mkdir -p "$TARGET_DIR"
    cp -r "$CURRENT_DIR"/* "$TARGET_DIR/"
fi

# 檢查 Python
if command -v python3 &>/dev/null; then
    echo "正在安裝必要 Python 套件 (edge-tts, pillow)..."
    python3 -m pip install -r "$TARGET_DIR/requirements.txt" -q
else
    echo "⚠️ 未找到 python3，請先安裝 Python 3.10+"
fi

# 檢查 FFmpeg
if command -v ffmpeg &>/dev/null; then
    echo "✓ FFmpeg 已就緒"
else
    echo "⚠️ 未找到 ffmpeg！請安裝 ffmpeg (macOS: brew install ffmpeg / Linux: sudo apt install ffmpeg)"
fi

echo ""
echo "🎉 安裝完成！已可直接在 Antigravity / Claude Code 中調用 /cinematic-micro-movie-architect"
