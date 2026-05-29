from app.rag.chain import ask_rag


question = "Why was Peter worried?"

response = ask_rag(question)

print("\nAI ANSWER:\n")

print(response["answer"])

print("\nSOURCES:\n")

for i, source in enumerate(response["sources"]):

    print(f"\nSOURCE {i+1}:\n")

    print(source.page_content[:300])

    print("\nMETADATA:")
    print(source.metadata)