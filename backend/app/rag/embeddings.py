'''
This file is responsible for:
converting text chunks into embeddings.

Embeddings are numerical vector representations of semantic meaning.

In production systems:

embedding models may change
providers may change
batching/caching may be added
inference optimization may be added

Keeping embeddings modular:

improves maintainability
simplifies scaling
makes architecture cleaner
'''

from langchain_huggingface import HuggingFaceEmbeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

'''This is:

lightweight
fast
free
widely used for semantic retrieval

Good engineering tradeoff for MVP-scale RAG systems.'''

