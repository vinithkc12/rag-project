# RAG Project (Retrieval Augmented Generation)

This project implements a simple RAG (Retrieval Augmented Generation) pipeline using:
- LangChain
- FAISS
- OpenAI / LLM
- FastAPI

The system loads PDF/text documents, creates embeddings, stores them in a vector database, and allows users to ask questions via an API.

---

## 📂 Project Structure
## How to Run

1. Clone repository
git clone https://github.com/vinithkc12/rag-project.git

2. Go to project folder
cd rag-project

3. Create virtual environment
python -m venv venv

4. Activate venv
venv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

6. Run API
uvicorn api:app --reload

Open browser:
http://127.0.0.1:8000/docs

## Example Question

POST /ask

{
  "question": "What is this document about?"
}


