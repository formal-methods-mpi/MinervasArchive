import os
import openai
import streamlit as st
from tempfile import NamedTemporaryFile

from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

def get_pages(pdf_file):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    loader = PyPDFLoader(pdf_file)
    pages = loader.load_and_split(text_splitter)
    return pages

def get_pages_from_upload(pdf_upload):
    with NamedTemporaryFile(dir='.', suffix='.pdf') as f:
        f.write(pdf_upload.getbuffer())
        pages = get_pages(f.name)
        return pages

def get_vectorstore(pages):
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL_NAME"), deployment=os.getenv("OPENAI_EMBEDDING_DEPLOYMENT_NAME"), chunk_size=1)
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_documents(documents=pages, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = AzureChatOpenAI(temperature=0, model=os.getenv("OPENAI_MODEL_NAME"), deployment_name=os.getenv("OPENAI_DEPLOYMENT_NAME"))
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory)
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    openai.api_type = os.getenv("OPENAI_API_TYPE")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_base = os.getenv("OPENAI_API_BASE") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
    openai.api_version = os.getenv("OPENAI_API_VERSION") # this may change in the future

    st.set_page_config(page_title="Chat with an PDF",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with an PDF :books:")
    user_question = st.text_input("Ask a question about your document:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your document")
        pdf_upload = st.file_uploader(
            "Upload your PDF here and click on 'Process'", accept_multiple_files=False, type='pdf')
        if st.button("Process"):
            with st.spinner("Processing"):
                pages = get_pages_from_upload(pdf_upload)

                # create vector store
                vectorstore = get_vectorstore(pages)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(
                    vectorstore)


if __name__ == '__main__':
    main()
