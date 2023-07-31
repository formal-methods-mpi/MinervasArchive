import prompts
from langchain.llms import AzureOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
import os
import streamlit as st

def simple_report_search(user_input):

    summarizer = AzureOpenAI(temperature=0, model="simple_report_search", deployment_name=os.getenv("OPENAI_SUMMARIZER_NAME"))
    
    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(summarizer,retriever=st.session_state.reportvectorstore.as_retriever(k=1))
    
    result = qa_chain({"question": user_input}, return_only_outputs=True)

    return result

def more_person_search(user_input):

    summarizer = AzureOpenAI(temperature=0, model="more_person_search", deployment_name=os.getenv("OPENAI_SUMMARIZER_NAME"))
    
    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(summarizer,retriever=st.session_state.personvectorstore.as_retriever(k=4))
    
    result = qa_chain({"question": user_input}, return_only_outputs=True)

    return result

def one_person_search(user_input):
    
    summarizer = AzureOpenAI(temperature=0, model="one_person_search", deployment_name=os.getenv("OPENAI_SUMMARIZER_NAME"))
    
    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(summarizer,retriever=st.session_state.personvectorstore.as_retriever(k=1))
    
    result = qa_chain({"question": user_input}, return_only_outputs=True)

    return result

def report_summarizer(user_input):

    summarizer = AzureOpenAI(temperature=0, model="report_summarizer", deployment_name=os.getenv("OPENAI_SUMMARIZER_NAME"))
    
    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(summarizer,retriever=st.session_state.reportvectorstore.as_retriever(k=4))
    
    result = qa_chain({"question": user_input}, return_only_outputs=True)
    
    return result
