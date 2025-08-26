from langchain_community.vectorstores import FAISS
from config import FAISS_DIR

def build_faiss_from_texts(texts, embeddings):
    vs = FAISS.from_texts(texts, embedding=embeddings)
    return vs

def save_faiss(vs):
    vs.save_local(FAISS_DIR)

def load_faiss(embeddings):
    return FAISS.load_local(FAISS_DIR, embeddings, allow_dangerous_deserialization=False)
