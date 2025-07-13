from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text_chunks):
    return model.encode(text_chunks, show_progress_bar=True)
