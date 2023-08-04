import os
import streamlit as st
#import embedFAISS as embed #For the FAISS vectorstore, uncomment only one
import embed #For the Chroma vectorstore, uncomment only one
from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from htmlTemplates import css, disclaimer_text, box_template, user_img, bot_img
import prompts
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.agents import AgentExecutor, LLMSingleActionAgent
from langchain import LLMChain
from typing import List
import agentTools as toolbox
from streamlit.components.v1 import html
import langchain

def get_conversation_chain(userinput):
    langchain.debug = True
    #Define AgentLLM
    moderator = AzureChatOpenAI(request_timeout=30,temperature=0.1, model="moderator", deployment_name=os.getenv("OPENAI_MODERATOR_NAME"))
    
    # initiate Toolbox
    tools=toolbox.create_tools()
    
    # create prompt for the agent (Includes behavior)
    prompt = embed.CustomPromptTemplate(
        template=prompts.moderatorSolo,
        tools=tools,
        input_variables=["input", "intermediate_steps", "history"]
    )

    # formate output
    output_parser = embed.CustomOutputParser()
    llm_chain = LLMChain(llm=moderator, prompt=prompt)
    tool_names = [tool.name for tool in tools]

    # Create agent
    agent = LLMSingleActionAgent(
        verbose=True, 
        llm_chain=llm_chain, 
        output_parser=output_parser,
        stop=["\nObservation:"], 
        allowed_tools=tool_names,
        handle_parsing_errors=True,
    )

    # combine agent and Tools for execution
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=st.session_state.conversation,handle_parsing_errors=True,)

    # execute
    answer = agent_executor.run(input=userinput)
    
    return answer

def handle_userinput(userinput, container):
    with st.spinner('Await the brilliance of Minerva, for in her wisdom lies the answers you seek...'):
        response = get_conversation_chain(userinput)

    # Update the session_state chat history with user question and chatbot response

    if st.session_state.chat_history is None:
        st.session_state.chat_history = [{'user': userinput, 'bot': response}]
    else:
        st.session_state.chat_history.append({'user': userinput, 'bot': response})
    display_chat_history(container)
    

def display_chat_history(container):
    with container:
        if st.session_state.chat_history is not None:
            for idx, chat in enumerate(st.session_state.chat_history):
                with st.chat_message("User",avatar=user_img):
                    st.write(chat['user'],unsafe_allow_html=True)
                with st.chat_message("Bot",avatar=bot_img):
                    st.write(chat['bot'],unsafe_allow_html=True)


def reset():
        st.session_state.user_question = st.session_state.widget
        st.session_state.widget = ''

def main():
    exec(open('auth.py').read())
    st.set_page_config(page_title="Chat with the research report",
                       page_icon=":books:",
                       initial_sidebar_state="collapsed")
    st.write(css, unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = ConversationBufferMemory(return_messages=True)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if 'user_question' not in st.session_state:
        st.session_state.user_question = ''
    if 'personvectorstore' not in st.session_state:
        st.session_state.personvectorstore = embed.person_vectorstore()
    if 'reportvectorstore' not in st.session_state:
        st.session_state.reportvectorstore = embed.report_vectorstore()
    
    
    #st.header("Chat with the research report:")
    #st.divider() 
    container=st.container()
    user_input = st.chat_input("Ask a question about the research report:")
    if user_input:
        handle_userinput(user_input, container)
    with st.container():
        st.caption(disclaimer_text)

    
    
if __name__ == '__main__':
    main()


