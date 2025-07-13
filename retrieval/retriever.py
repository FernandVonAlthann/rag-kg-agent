from retrieval.embedder import embed_text
from retrieval.vector_store import search

def retrieve(query):
    query_embedding = embed_text([query])[0]
    indices = search(query_embedding)
    dummy_docs = [
        "John Doe filed a report last Monday.",
        "He met with the board on Tuesday.",
        "Wednesday was focused on R&D efforts.",
        "Thursday involved a press briefing.",
        "Friday was a cleanup of action items."
    ]
    return [dummy_docs[i] for i in indices[0]]
