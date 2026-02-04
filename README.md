# RAG Project (Retrieval Augmented Generation)

A simple Retrieval Augmented Generation (RAG) system built using LangChain, FAISS, OpenAI LLM, and FastAPI.  
This project allows users to upload documents and ask questions based on the content.

---

## 🚀 Features

- Load PDF and TXT documents  
- Create embeddings and store in FAISS vector database  
- Retrieve relevant context for user queries  
- Generate answers using LLM  
- REST API using FastAPI  

---

## 🛠 Tech Stack

- Python  
- LangChain  
- FAISS  
- OpenAI  
- FastAPI  

---

## 📂 Project Structure
rag-project/ │ ├── api.py ├── requirements.txt ├── README.md │ ├── data/ │   ├── sample.txt │   └── Vinith GenAI.pdf │ ├── rag/ │   ├── init.py │   ├── loader.py │   ├── vectorstore.py │   └── llm.py │ └── venv/

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

python -m venv venv
Activate:
venv\Scripts\activate
---

### 2️⃣ Install Dependencies
pip install -r requirements.txt
---

### 3️⃣ Set OpenAI API Key (Windows)
setx OPENAI_API_KEY "your_api_key_here"
Restart terminal after this.

---

### 4️⃣ Run Application
uvicorn api:app --reload
Open browser:
http://127.0.0.1:8000/docs
---

## 📌 Example API Request

POST `/ask`
{ "question": "What is this document about?" }
---

## ✅ Output

Returns an answer generated using your uploaded documents.

---

## 📈 Future Improvements

- Add authentication  
- Add UI using Streamlit  
- Add multi-document upload  
- Add chat history  

---

## 👨‍💻 Author

Vinith Kumar  
GenAI / Python Developer

