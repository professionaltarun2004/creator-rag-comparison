'''
This file creates:

the conversational RAG API endpoint.

Responsibilities:

receive user questions
trigger semantic retrieval
generate grounded AI responses
return sources/citations

This endpoint becomes:

the primary intelligence interface of your application.
'''

from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.rag.chain import ask_rag

router=APIRouter() 

@router.post("/chat") 

def chat(request: ChatRequest):
    response=ask_rag(request.question)
    formatted_sources=[]
    for source in response["sources"]:
        formatted_sources.append(
            {
                "content":source.page_content,
                "metadata":source.metadata
            }
        )
    
    return {
        "answer":response["answer"],
        "sources":formatted_sources
    }