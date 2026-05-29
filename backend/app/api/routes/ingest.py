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

router=APIRouter()

@router.post("/ingest")

def ingest_video(request: IngestRequest):

    #extract transcript
    data=get_youtube_transcript(request.url)

    #chunk transcript
    chunks=chunk_text(data["transcript"])

    #store embeddings in vector DB
    store_chunks(
        chunks=chunks,
        video_id=data["video_id"]
    )

    #return response
    return {
        "message": "Video ingested successfully",
        "video_id":data["video_id"],
        "total_chunks":len(chunks)
    }