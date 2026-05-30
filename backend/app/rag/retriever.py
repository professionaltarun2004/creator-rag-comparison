from langchain_community.vectorstores import Chroma

from app.rag.embeddings import embedding_model

VECTOR_DB_PATH = "chroma_db"


def retrieve_video_chunks(query, video_id):

    vector_store = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding_model
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 3,
            "fetch_k": 10,
            "filter": {
                "video_id": video_id
            }
        }
    )

    results = retriever.invoke(query)

    return results