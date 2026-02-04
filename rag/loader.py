from pathlib import Path

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_DIR = Path("data")

def load_docs():
    documents = []

    # Load TXT files
    for txt_file in DATA_DIR.rglob("*.txt"):
        loader = TextLoader(str(txt_file), encoding="utf-8")
        documents.extend(loader.load())

    # Load PDF files
    for pdf_file in DATA_DIR.rglob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)