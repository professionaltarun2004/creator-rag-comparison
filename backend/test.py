from app.services.youtube_service import get_youtube_transcript
from app.rag.chunking import chunk_text
from app.rag.vector_store import store_chunks


url = "https://www.youtube.com/watch?v=OZQgtnh58Jo"

data = get_youtube_transcript(url)

chunks = chunk_text(data["transcript"])

vector_store = store_chunks(
    chunks=chunks,
    video_id=data["video_id"]
)

print("\nChunks stored successfully in ChromaDB.")
print(f"\nTotal chunks stored: {len(chunks)}")