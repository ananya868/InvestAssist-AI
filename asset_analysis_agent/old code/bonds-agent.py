import pandas as pd 
import spacy 
import json
import os 
import PyPDF2
import pprint
from dotenv import load_dotenv

import crewai
from crewai import Agent, Task, Crew, tools


# load env vars from .env file 
load_dotenv()


os.environ["OPENAI_MODEL_NAME"] = 'gpt-4-turbo'
# Api keys 
openai_api_key = os.getenv("OPENAI_API_KEY")

from crewai_tools import EXASearchTool

# Initialize the tool for internet searching capabilities
exa_tool = EXASearchTool()



"""Agent"""


bonds_data_agent = Agent(
    role = 'Bonds Data Collector', 
    goal = 'The Bond Data Collector Agent is responsible for searching the internet for real-time data on bonds in both domestic and international markets. '
            'It focuses exclusively on collecting data for the {current_date}, ensuring that all information is up-to-date and relevant. The gathered data is essential for optimizing investors portfolios',
    backstory = """'The Bond Data Collector Agent was conceived to address the increasing need for timely and accurate bond market data in portfolio optimization.'
            'Bonds play a crucial role in diversified investment strategies, and having access to real-time data is imperative for making informed investment decisions. '
            'This agent was developed to automate the process of data collection, ensuring that investors have the most current bond information at their fingertips.'
            'Over time, the agent has evolved to handle a wide range of data sources, integrating seamlessly with other components of the portfolio optimization system.'""",
    allow_delegation = True,
    verbose = True
)   

task = """Real-time bond prices for domestic and international markets Yields, maturities, and ratings of the bonds.
        Relevant bond metrics and indicators.
        A timestamp indicating the collection date {current_date}."""

bonds_data_task = Task(
    description = "Search the internet for real-time data on domestic and international bonds."
            "Collect data exclusively for the date: {current_date} to ensure relevance."
            "Make sure to get the following information by: {task}"
            "Ensure data accuracy and completeness by cross-referencing multiple sources.",
    expected_output = "The expected output of the Bond Data Collector Agent is Markdown format document with each data sections containing all the details",
    tools = [exa_tool],
    agent = bonds_data_agent,
)



crew = Crew(
    agents = [bonds_data_agent],
    
    tasks = [bonds_data_task],
	
    verbose = 2,
    memory = True
)


crew.kickoff(inputs = {
        'current_date': '2024-09-15',
        'task': task
})





