from langchain.agents import Tool
from htmlTemplates import css, bot_template, user_template, disclaimer_text, box_template, user_img, bot_img
from typing import List
from langchain.agents import Tool
from streamlit.components.v1 import html
from agentFunctions import simple_report_search, report_summarizer, one_person_search, tearm_search

def create_tools():
    # define usable Tools for the Agent
    tools = [
        Tool(
            name = "TermSearch",
            func=tearm_search,
            description="Search for specific terms to clarify their meaning. Input the desired term."
        ),
        Tool(
            name = "SimpleReportSearch",
            func=simple_report_search,
            description="Retrieve concise information from the report, especially about groups, projects, schools, or members of a group. Input your question and related keywords."
        ),
        Tool(
            name = "ReportSummarizer",
            func = report_summarizer,
            description="Extract comprehensive details from the report when broader context is needed. Input your question and related keywords."
        ),
        Tool(
            name = "OnePersonSearch",
            func= one_person_search,
            description="Locate specific details about a person in the MPI. Input the person's name and any related query."
        )
    ]
    return tools
