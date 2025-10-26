import json
import subprocess
import os
import webvtt
from deep_translator import GoogleTranslator

# === CONFIG ===
video_url = input("Paste YouTube video URL: ").strip()
output_json = "transcript.json"

try:
    print("▶ Downloading available subtitles using yt-dlp...")

    # Step 1: Download any auto-generated subtitles (browser UA to avoid 429)
    subprocess.run(
        [
            "yt-dlp",
            "--write-auto-sub",
            "--skip-download",
            "--sub-langs", "all",
            "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
            "--output", "subtitles",
            video_url
        ],
        check=True,
        capture_output=True,
        text=True
    )

    # Step 2: Find downloaded .vtt file
    vtt_file = None
    for file in os.listdir():
        if file.startswith("subtitles") and file.endswith(".vtt"):
            vtt_file = file
            break

    if not vtt_file:
        raise FileNotFoundError(
            "No subtitle file found (auto-generated subtitles may be disabled)."
        )

    print(f"✅ Found subtitles: {vtt_file}")

    # Step 3: Parse VTT and convert to clean JSON
    transcript_data = []
    for caption in webvtt.read(vtt_file):
        h, m, s = [float(x.replace(",", ".")) for x in caption.start.split(":")]
        start_seconds = h * 3600 + m * 60 + s
        text = caption.text.replace("\n", " ").strip()
        if text:
            transcript_data.append({"start": round(start_seconds, 2), "text": text})

    # Step 4: Translate to English (if not already)
    print("▶ Translating transcript to English...")
    translator = GoogleTranslator(source='auto', target='en')
    for entry in transcript_data:
        try:
            entry["text"] = translator.translate(entry["text"])
        except Exception as e:
            print(f"⚠️ Translation failed for: {entry['text']}, error: {e}")

    # Step 5: Save cleaned JSON
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(transcript_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Transcript saved to {output_json}")
    print(json.dumps(transcript_data[:5], indent=2, ensure_ascii=False))  # Preview first 5

except subprocess.CalledProcessError as e:
    print("❌ yt-dlp failed:\n", e.stderr)
except Exception as e:
    print("❌ Error:", e)

