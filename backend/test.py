from app.services.youtube_service import get_youtube_transcript
from app.rag.chunking import chunk_text

url = "https://www.youtube.com/watch?v=GWnSsjT4V68&list=PLKnIA16_RmvYsvB8qkUQuJmJNuiCUJFPL&index=4"

data = get_youtube_transcript(url)

chunks = chunk_text(data["transcript"])

print("\nTOTAL CHUNKS:\n")
print(len(chunks))

print("\nFIRST CHUNK:\n")
print(chunks[0])

print("\nSECOND CHUNK:\n")
print(chunks[1])