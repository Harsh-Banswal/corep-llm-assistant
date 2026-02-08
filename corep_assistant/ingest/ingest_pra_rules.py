from pathlib import Path
import pickle
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

# Load PRA Own Funds text
file_path = Path("data/pra_rules/own_funds_crr_phase0.txt")
text = file_path.read_text(encoding="utf-8")

# Simple chunking function
def chunk_text(text, chunk_size=400, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

chunks = chunk_text(text)

# Vectorize with TF-IDF
vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(chunks)

# Build FAISS index
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(vectors.toarray().astype("float32"))

# Save artifacts
Path("vectorstore").mkdir(exist_ok=True)

faiss.write_index(index, "vectorstore/pra_own_funds.index")

with open("vectorstore/pra_own_funds_chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

with open("vectorstore/pra_own_funds_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print(f"Phase 2 ingestion complete. Chunks created: {len(chunks)}")
