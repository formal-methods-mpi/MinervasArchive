import os
import streamlit as st
import shutil
from tempfile import NamedTemporaryFile
import embed
from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

def pages_from_upload(pdf_upload):
    with NamedTemporaryFile(dir='.', suffix='.pdf') as f:
        f.write(pdf_upload.getbuffer())
        pages = embed.pages(f.name)
        return pages

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


def handle_userinput(user_question, vectorstore):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            answer = message.content
            doc = vectorstore.similarity_search(answer, k=1)
            page = doc[0].metadata["page"] + 1
            answer = answer + "\n\nPage: " + str(page)
            st.write(bot_template.replace(
                "{{MSG}}", answer), unsafe_allow_html=True)


def main():
    exec(open('auth.py').read())
    st.set_page_config(page_title="Chat with an PDF",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "vectorstore2" not in st.session_state:
        st.session_state.vectorstore2 = None

    st.header("Chat with an PDF :books:")
    user_question = st.text_input("Ask a question about your document:")
    if user_question:
        handle_userinput(user_question, st.session_state.vectorstore2)

    with st.sidebar:
        if embed.db_dir_exists():
            st.subheader("Your Database")
            if st.button("Delete"):
                try:
                    shutil.rmtree(embed.db_dir())
                    os.rmdir(embed.db_dir())
                    st.experimental_rerun()
                finally:
                    None
            # create conversation chain
            vectorstore = embed.vectorstore()
            st.session_state.vectorstore2 = embed.vectorstore()
            st.session_state.conversation = get_conversation_chain(vectorstore)
        else:
                st.subheader("Your document")
                pdf_upload = st.file_uploader(
                    "Upload your PDF here and click on 'Process'", accept_multiple_files=False, type='pdf')
                if st.button("Process"):
                    with st.spinner("Processing"):
                        pages = pages_from_upload(pdf_upload)
                        # create vector store
                        vectorstore = embed.pages_to_vectorstore(pages)
                        vectorstore.persist()
                        st.experimental_rerun()


if __name__ == '__main__':
    main()
