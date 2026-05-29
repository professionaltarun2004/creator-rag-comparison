from app.rag.retriever import retrieve_relevant_chunks


query = "Why was Peter worried?"

results = retrieve_relevant_chunks(query)

print("\nRetrieved Chunks:\n")

for i, result in enumerate(results):

    print(f"\nRESULT {i+1}:\n")

    print(result.page_content)

    print("\nMETADATA:")
    print(result.metadata)