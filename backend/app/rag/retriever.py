from langchain_community.vectorstores import Chroma
from app.rag.embeddings import embedding_model

VECTOR_DB_PATH="chroma_db"

def retrieve_relevant_chunks(query):
    vector_store=Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding_model
    )

    results=vector_store.similarity_search(
        query=query,
        k=3
    )
    '''
    k=3

    Retrieve top 3 most relevant chunks.

    Good starting point.
    '''

    return results