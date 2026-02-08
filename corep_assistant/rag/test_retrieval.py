import pickle
import faiss
import numpy as np

# Load FAISS index
index = faiss.read_index("vectorstore/pra_own_funds.index")

with open("vectorstore/pra_own_funds_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

with open("vectorstore/pra_own_funds_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Query
query = "What is Common Equity Tier 1 capital?"
query_vec = vectorizer.transform([query]).toarray().astype("float32")

# Search
D, I = index.search(query_vec, k=3)

print("\nTop results:")
for rank, idx in enumerate(I[0], 1):
    print(f"\nResult {rank}:")
    print(chunks[idx])
