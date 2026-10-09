<#
.SYNOPSIS
  Cinematic Micro-Movie Architect 一鍵安裝腳本 (Windows)
#>

$ErrorActionPreference = "Stop"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "🎬 正在安裝 Cinematic Micro-Movie Architect 技能 (Windows)..." -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. 目標技能路徑
$targetDir = "$env:USERPROFILE\.gemini\config\skills\cinematic-micro-movie-architect"
$currentDir = $PSScriptRoot

if ($currentDir -ne $targetDir) {
    Write-Host "正在部署檔案至: $targetDir" -ForegroundColor Yellow
    if (-not (Test-Path $targetDir)) {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    }
    Copy-Item -Path "$currentDir\*" -Destination $targetDir -Recurse -Force
}

# 2. 檢查 Python
Write-Host "檢查 Python 環境..." -ForegroundColor Yellow
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) {
    Write-Warning "未找到 Python！請安裝 Python 3.10 以上版本。"
} else {
    Write-Host "正在安裝必要 Python 套件 (edge-tts, pillow)..." -ForegroundColor Yellow
    & python -m pip install -r "$targetDir\requirements.txt" --quiet
}

# 3. 檢查 FFmpeg
Write-Host "檢查 FFmpeg 環境..." -ForegroundColor Yellow
$ffmpeg = Get-Command ffmpeg -ErrorAction SilentlyContinue
if (-not $ffmpeg) {
    Write-Warning "未偵測到 FFmpeg！建議執行: winget install Gyan.FFmpeg"
} else {
    Write-Host "✓ FFmpeg 已就緒: $($ffmpeg.Source)" -ForegroundColor Green
}

Write-Host ""
Write-Host "🎉 安裝完成！您已可在 Antigravity 中直接使用 /cinematic-micro-movie-architect 指令！" -ForegroundColor Green
