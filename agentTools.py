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
            description="useful if you only need a little bit of information from the MPI Research Report 2023, because the User Question is simple"
        ),
        Tool(
            name = "ReportSummarizer",
            func = report_summarizer,
            description="useful if you need a lot information from the MPI Research Report 2023"
        ),
        Tool(
            name = "OnePersonSearch",
            func= one_person_search,
            description="useful when you need information about only one persons in the MPI"
        ),
        Tool(
            name = "MorePersonSearch",
            func=more_person_search,
            description="useful when you need information about more then one persons in the MPI"
        )
    ]
    return tools
