"""
Cinematic Micro-Movie Pipeline
Automates: Edge-TTS generation -> Procedural BGM -> Ken Burns Video Rendering -> ASS Subtitles -> Master MP4 Output
"""

import asyncio
import math
import os
import random
import struct
import subprocess
import wave
import edge_tts

def generate_procedural_bgm(output_path, total_duration=56.0, sample_rate=44100):
    """Generates procedural cinematic war drum background music using pure python standard library."""
    num_samples = int(total_duration * sample_rate)
    left_channel = [0.0] * num_samples
    right_channel = [0.0] * num_samples
    rng = random.Random(42)

    # Low drone
    for i in range(num_samples):
        t = i / sample_rate
        envelope = 0.15 + 0.08 * math.sin(2 * math.pi * 0.1 * t)
        if t < 3.0:
            envelope *= (t / 3.0)
        elif t > total_duration - 4.0:
            envelope *= ((total_duration - t) / 4.0)
        drone = (
            0.5 * math.sin(2 * math.pi * 55.0 * t) +
            0.3 * math.sin(2 * math.pi * 82.4 * t) +
            0.2 * math.sin(2 * math.pi * 110.0 * t)
        ) * envelope
        left_channel[i] += drone * 0.95
        right_channel[i] += drone * 1.05

    def add_drum(start_time, intensity=1.0, pitch=60.0, decay=1.2):
        start_idx = int(start_time * sample_rate)
        length = int(decay * sample_rate)
        for j in range(length):
            idx = start_idx + j
            if idx >= num_samples:
                break
            dt = j / sample_rate
            amp = math.exp(-4.5 * dt / decay) * intensity
            cur_pitch = pitch * (1.0 + 1.2 * math.exp(-15.0 * dt))
            val = math.sin(2 * math.pi * cur_pitch * dt) * amp
            noise = (rng.random() * 2 - 1) * amp * 0.25 * math.exp(-8.0 * dt)
            left_channel[idx] += (val + noise) * 0.9
            right_channel[idx] += (val + noise) * 1.1

    def add_gong(start_time, intensity=0.7, decay=3.5):
        start_idx = int(start_time * sample_rate)
        length = int(decay * sample_rate)
        for j in range(length):
            idx = start_idx + j
            if idx >= num_samples:
                break
            dt = j / sample_rate
            amp = math.exp(-1.8 * dt) * intensity
            val = (
                math.sin(2 * math.pi * 320 * dt) * 0.25 +
                math.sin(2 * math.pi * 480 * dt) * 0.25 +
                math.sin(2 * math.pi * 710 * dt) * 0.25
            ) * amp
            left_channel[idx] += val
            right_channel[idx] += val

    # Beats
    for beat in range(1, 7):
        add_drum(beat * 2.0, intensity=0.8, pitch=58.0)
    t = 14.0
    add_gong(14.0, intensity=0.8)
    while t < 26.5:
        add_drum(t, intensity=0.9, pitch=68.0, decay=0.8)
        add_drum(t + 0.35, intensity=0.7, pitch=75.0, decay=0.6)
        t += 1.2
    for k in range(12):
        add_drum(25.0 + k * 0.15, intensity=0.5 + k * 0.05, pitch=80.0 + k * 3.0, decay=0.3)
    add_gong(27.0, intensity=1.0, decay=4.5)
    add_drum(27.0, intensity=1.3, pitch=50.0, decay=2.0)
    for beat in range(1, 9):
        add_drum(27.0 + beat * 1.8, intensity=1.0, pitch=54.0, decay=1.5)
    add_gong(43.0, intensity=0.9, decay=5.0)
    add_drum(43.0, intensity=1.1, pitch=52.0, decay=2.5)

    max_amp = max(max(abs(x) for x in left_channel), max(abs(x) for x in right_channel))
    scale = (0.85 / max_amp) if max_amp > 0 else 1.0

    with wave.open(output_path, "w") as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        for i in range(num_samples):
            l = int(max(-32767, min(32767, left_channel[i] * scale * 32767)))
            r = int(max(-32767, min(32767, right_channel[i] * scale * 32767)))
            wav_file.writeframes(struct.pack("<hh", l, r))

async def generate_voices(scripts, output_dir, voice="zh-CN-YunjianNeural"):
    """Generates speech mp3s for each script block."""
    for s in scripts:
        out_path = os.path.join(output_dir, f"{s['id']}_voice.mp3")
        c = edge_tts.Communicate(s["text"], voice, rate="-5%", pitch="-2Hz")
        await c.save(out_path)

def render_ken_burns_clip(image_path, output_clip, duration, zoom_expr):
    """Renders a single image into a smooth Ken Burns MP4 clip."""
    cmd = [
        "ffmpeg", "-y", "-loop", "1",
        "-i", image_path,
        "-vf", f"scale=2560:-1,{zoom_expr}",
        "-t", str(duration),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-preset", "veryfast", "-crf", "18",
        output_clip
    ]
    subprocess.run(cmd, check=True)

print("Cinematic Micro-Movie Pipeline ready.")
