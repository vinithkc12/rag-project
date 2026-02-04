from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

vectorstore = None

def build_vectorstore(chunks):
    global vectorstore

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"   # best local embedding model
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore