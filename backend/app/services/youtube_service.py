from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse,parse_qs

def extract_video_id(url:str):
    passed_url=urlparse(url)

    # Shortened youtu.be links
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    # Standard youtube links
    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    return None

def get_youtube_transcript(url:str):
    video_id=extract_video_id(url)
    transcript=YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry["text"] for entry in transcript])

    return {
        "video_id": video_id,
        "transcript": full_text
    }