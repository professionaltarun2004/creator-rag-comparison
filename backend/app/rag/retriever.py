from langchain_community.vectorstores import Chroma
from app.rag.embeddings import embedding_model

VECTOR_DB_PATH="chroma_db"

def retrieve_relevant_chunks(query):
    vector_store=Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding_model
    )

    # results=vector_store.similarity_search(
    #     query=query,
    #     k=3
    # )
    '''
    k=3

    Retrieve top 3 most relevant chunks.

    Good starting point.
    '''

    retriever=vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k":3,
            "fetch_k":10
        }
    )

    '''
    PURPOSE UPDATE

    This file now becomes responsible for:

    semantic similarity
    retrieval diversity optimization

    This improves:

    contextual coverage
    answer quality
    source quality.


    MMR tries to:

    keep chunks relevant
    reduce duplication
    improve coverage diversity

    This is MUCH closer to production RAG behavior.
    '''

    results = retriever.invoke(query)


    return results