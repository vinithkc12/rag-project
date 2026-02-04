from fastapi import FastAPI, HTTPException
from rag.loader import load_docs
from rag.vectorstore import build_vectorstore

app = FastAPI()

vectorstore = None

@app.on_event("startup")
def startup_event():
    global vectorstore
    try:
        documents = load_docs()
        print(f"Loaded {len(documents)} documents")

        vectorstore = build_vectorstore(documents)
        print("Vectorstore loaded successfully")

    except Exception as e:
        print("Startup failed:", e)
        vectorstore = None

@app.get("/")
def root():
    return {"message": "API is working"}

from rag.llm import get_llm

@app.get("/ask")
def ask(q: str):
    if vectorstore is None:
        raise HTTPException(status_code=500, detail="Vectorstore not loaded")

    docs = vectorstore.similarity_search(q, k=4)

    context = "\n\n".join(doc.page_content for doc in docs)

    llm = get_llm()

    prompt = f"""
You are an AI assistant. Use the following CV content to answer the question.

CV CONTENT:
{context}

QUESTION:
{q}

Give a clear and professional answer.
"""

    response = llm.invoke(prompt)

    return {"answer": response.content}