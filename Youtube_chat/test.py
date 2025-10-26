from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

video_id = "LPZh9BOjkQs"

try:
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    print("✅ Available transcripts:")
    for t in transcript_list:
        print(f" - {t.language_code} ({'auto-generated' if t.is_generated else 'manual'})")

    # Try to get a translated transcript (fallback if direct fetch fails)
    try:
        transcript = transcript_list.find_transcript(['en'])
        data = transcript.fetch()
    except Exception:
        print("⚠️ Direct fetch failed, trying translation API...")
        transcript = transcript_list.find_transcript(['en']).translate('en')
        data = transcript.fetch()

    text = " ".join(chunk["text"] for chunk in data)
    print("\n📝 Transcript preview:")
    print(text[:500])

except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video")

except NoTranscriptFound:
    print("❌ No transcript available in the requested languages")

except Exception as e:
    print("⚠️ Unexpected error:", e)


