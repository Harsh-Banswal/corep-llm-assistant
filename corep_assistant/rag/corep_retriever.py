import pickle
import faiss

from schemas.corep_c01_schema import CorepField

# Load FAISS index
index = faiss.read_index("vectorstore/pra_own_funds.index")

with open("vectorstore/pra_own_funds_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

with open("vectorstore/pra_own_funds_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def retrieve_for_corep_field(corep_field: CorepField, k=2):
    """
    Retrieve PRA regulatory text relevant to a COREP field
    """
    query = " ".join(corep_field.regulatory_concepts)
    query_vec = vectorizer.transform([query]).toarray().astype("float32")

    D, I = index.search(query_vec, k=k)

    results = []
    for idx in I[0]:
        results.append(chunks[idx])

    return results

