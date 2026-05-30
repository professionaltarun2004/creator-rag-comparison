from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.rag.chain import compare_videos

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    response = compare_videos(
        question=request.question,
        video_a=request.video_a,
        video_b=request.video_b
    )

    formatted_video_a_sources = []

    for source in response["video_a_sources"]:

        formatted_video_a_sources.append({
            "content": source.page_content,
            "metadata": source.metadata
        })

    formatted_video_b_sources = []

    for source in response["video_b_sources"]:

        formatted_video_b_sources.append({
            "content": source.page_content,
            "metadata": source.metadata
        })

    return {
        "answer": response["answer"],
        "video_a_sources": formatted_video_a_sources,
        "video_b_sources": formatted_video_b_sources
    }