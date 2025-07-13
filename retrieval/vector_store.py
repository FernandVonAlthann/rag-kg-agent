import faiss
import numpy as np
import os

dimension = 384  # for all-MiniLM-L6-v2
index = faiss.IndexFlatL2(dimension)

def add_embeddings(embeddings):
    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)

def search(query_embedding, k=5):
    query = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query, k)
    return indices
