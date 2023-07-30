from langchain.agents import Tool
from htmlTemplates import css, bot_template, user_template, disclaimer_text, box_template, user_img, bot_img
from typing import List
from langchain.agents import Tool
from streamlit.components.v1 import html
from agentFunctions import simple_report_search, report_summarizer, one_person_search, more_person_search

def create_tools():
    # define usable Tools for the Agent
    tools = [
        Tool(
            name = "SimpleReportSearch",
            func=simple_report_search,
            description="useful if you only need a little bit of information from the MPI Research Report 2023, because the User Question is simple. Input the question and the keywords for a keyword-based search in a vector space"
        ),
        Tool(
            name = "ReportSummarizer",
            func = report_summarizer,
            description="useful if you need a lot information from the MPI Research Report 2023. Input the question and the keywords for a keyword-based search in a vector space"
        ),
        Tool(
            name = "OnePersonSearch",
            func= one_person_search,
            description="useful when you need personal information about only one persons in the MPI. It will list references for Selected Literature of this person aswell. Input the question and the name of the person"
        ),
        Tool(
            name = "MorePersonSearch",
            func=more_person_search,
            description="useful when you need information about more then one persons in the MPI. It will list references for Selected Literature of this person aswell. Input the question and all names of all the persons"
        )
    ]
    return tools
