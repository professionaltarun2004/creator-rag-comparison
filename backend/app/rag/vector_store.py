'''This file is responsible for:

storing transcript chunk embeddings inside ChromaDB.

Think of it as:

semantic memory storage for your chatbot.

Instead of storing:

normal rows and columns

we store:

chunk text
embeddings
metadata

This allows:

semantic similarity search
contextual retrieval
source citations
'''

from langchain_community.vectorstores import Chroma
from app.rag.embeddings import embedding_model

VECTOR_DB_PATH="chroma_db"

def store_chunks(chunks,video_id):
    texts=[]
    metadatas=[]

    for chunk in chunks:
        texts.append(chunk)
        metadatas.append(
            {
                "video_id":video_id
            }
        )
    
    vector_store=Chroma.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas,
        persist_directory=VECTOR_DB_PATH
    )

    return vector_store
