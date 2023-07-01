"A module for embeding PDFs into a vector database"

import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def pages(pdf_file):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    loader = PyPDFLoader(pdf_file)
    pages = loader.load_and_split(text_splitter)
    return pages

def vectorstore(pages):
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL_NAME"), deployment=os.getenv("OPENAI_EMBEDDING_DEPLOYMENT_NAME"), chunk_size=1)
    vectorstore = FAISS.from_documents(documents=pages, embedding=embeddings)
    return vectorstore
