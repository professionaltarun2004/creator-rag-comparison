from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str):

    parsed_url = urlparse(url)

    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    return None


def get_youtube_transcript(url: str):

    video_id = extract_video_id(url)

    ytt_api = YouTubeTranscriptApi()

    transcript_data = ytt_api.fetch(video_id, languages=["hi", "en"])

    full_text = " ".join([snippet.text for snippet in transcript_data])

    return {
        "video_id": video_id,
        "transcript": full_text
    }