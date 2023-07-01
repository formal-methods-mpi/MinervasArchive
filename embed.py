"A module for embeding PDFs into a vector database"

import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

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

def db_dir():
    load_dotenv()
    return os.getenv("CHROMA_DIR")

def db_dir_exists():
    return os.path.isdir(db_dir())

def embedding():
    return OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL_NAME"), deployment=os.getenv("OPENAI_EMBEDDING_DEPLOYMENT_NAME"), chunk_size=1)

def pages_to_vectorstore(pages):
    vectorstore = Chroma.from_documents(documents=pages, embedding=embedding(), persist_directory=db_dir())
    return vectorstore

def vectorstore():
    return Chroma(persist_directory=db_dir(), embedding_function=embedding())
