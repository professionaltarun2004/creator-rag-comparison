'''
This file creates:

transcript ingestion API endpoint.

This endpoint will:

accept video URL
extract transcript
chunk transcript
create embeddings
store vectors

This becomes:

your ingestion pipeline endpoint.
'''

from fastapi import APIRouter

from app.models.schemas import IngestRequest

from app.services.youtube_service import get_youtube_transcript

from app.rag.chunking import chunk_text
from app.rag.vector_store import store_chunks


router = APIRouter()


@router.post("/ingest")
def ingest_video(request: IngestRequest):

    #Extract transcript
    data = get_youtube_transcript(request.url)

    #Chunk transcript
    chunks = chunk_text(data["transcript"])

    #Build metadata
    metadata = {
        "video_id": data["video_id"],
        "platform": "youtube",
        "creator": "unknown",
        "views": 0,
        "likes": 0,
        "comments": 0,
        "engagement_rate": 0
    }

    #Store chunks
    store_chunks(
        chunks=chunks,
        metadata=metadata
    )

    return {
        "message": "Video ingested successfully",
        "video_id": data["video_id"],
        "total_chunks": len(chunks),
        "metadata": metadata
    }