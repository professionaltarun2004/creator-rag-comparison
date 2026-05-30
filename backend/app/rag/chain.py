import os
from dotenv import load_dotenv
from openai import OpenAI
from app.rag.retriever import retrieve_video_chunks
from app.rag.memory import get_memory, add_to_memory

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def compare_videos(question, video_a, video_b):

    video_a_docs = retrieve_video_chunks(
        question,
        video_a
    )

    video_b_docs = retrieve_video_chunks(
        question,
        video_b
    )

    video_a_context = "\n\n".join(
        [doc.page_content for doc in video_a_docs]
    )

    video_b_context = "\n\n".join(
        [doc.page_content for doc in video_b_docs]
    )

    memory=get_memory()

    memory_context="\n".join(
        [
            f"{item['role']}:{item['content']}"
            for item in memory
        ]
    )

    prompt = f"""
                You are an AI creator intelligence assistant.

                Previous Conversation:
                {memory_context}

                Analyze and compare two videos.

                VIDEO A TRANSCRIPT CONTEXT:
                {video_a_context}

                VIDEO B TRANSCRIPT CONTEXT:
                {video_b_context}

                QUESTION:
                {question}

                Provide:
                1. Clear comparison
                2. Engagement reasoning
                3. Hook analysis
                4. Content strategy insights
                5. Improvement suggestions
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

    add_to_memory(
        "user",
        question
    )

    add_to_memory(
        "assistant",
        answer
    )

    return {
        "answer": answer,
        "video_a_sources": video_a_docs,
        "video_b_sources": video_b_docs
    }