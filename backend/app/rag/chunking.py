''' 
PURPOSE OF THIS FILE

This file is responsible for:

splitting large transcript text into smaller semantic chunks.

This is required because:

LLMs cannot efficiently process massive transcripts
vector databases store smaller chunks better
retrieval quality improves with meaningful chunk sizes
'''

from langchain_text_splitters import RecursiveCharacterTextSplitter

'''
RecursiveCharacterTextSplitter

Smart splitter from LangChain.

It:

tries preserving sentence structure
avoids ugly random cuts
creates better semantic chunks
'''

def chunk_text(text:str):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    '''
    chunk_size=800
    Each chunk ≈ 800 characters.

    Good balance between:

    context
    retrieval precision

    chunk_overlap=100

    Repeats 100 characters into next chunk.

    Improves:

    semantic continuity
    retrieval quality
    '''

    chunks=splitter.split_text(text)
    return chunks