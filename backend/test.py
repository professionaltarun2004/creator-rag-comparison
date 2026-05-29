from app.services.youtube_service import get_youtube_transcript 

url="https://www.youtube.com/watch?v=GWnSsjT4V68&list=PLKnIA16_RmvYsvB8qkUQuJmJNuiCUJFPL&index=4"
data=get_youtube_transcript(url)

print("\nvideo id:\n")
print(data["video_id"])

print("\nTRANSCRIPT:\n")
print(data["transcript"][:1000])