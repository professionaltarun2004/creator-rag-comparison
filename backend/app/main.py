from fastapi import FastAPI
from app.api.routes.ingest import router as ingest_router
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="Creator RAG API"
)

@app.get("/")

def home():
    return {
        "message":"Creator RAG Backend Running"
    }

#register ingestion routes
app.include_router(ingest_router)
app.include_router(chat_router)