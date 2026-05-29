'''
This file orchestrates:

semantic retrieval
prompt construction
Gemini generation
source return

It is the:

reasoning layer of your RAG system.

This is where:
retrieval + LLM combine together.
'''


import os

from dotenv import load_dotenv

from openai import OpenAI

from app.rag.retriever import retrieve_relevant_chunks


load_dotenv()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def ask_rag(question: str):

    retrieved_docs = retrieve_relevant_chunks(question)

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = f"""
You are an AI assistant analyzing social media video transcripts.

Use ONLY the provided context to answer.

CONTEXT:
{context}

QUESTION:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer,
        "sources": retrieved_docs
    }