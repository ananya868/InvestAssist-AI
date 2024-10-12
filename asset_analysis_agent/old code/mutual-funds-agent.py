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


"""Agent"""


mutual_fund_data_agent = Agent(
    role = 'Mutual Fund Data Collector', 
    goal = 'The Mutual Fund Data Collector Agent is responsible for searching the internet for real-time data on mutual funds in both domestic and international markets.'
            'It focuses exclusively on collecting data for the current date, ensuring that all information is up-to-date and relevant.'
            ' The gathered data is essential for optimizing investors portfolios',
    backstory = 'The Mutual Fund Data Collector Agent was developed to address the growing need for timely and accurate mutual fund market data in portfolio optimization.'
            'Mutual funds are a critical component of diversified investment strategies, and access to real-time data is crucial for making informed investment decisions.'
            'This agent was created to automate the process of data collection, ensuring that investors have the most current mutual fund information. '
            'Over time, the agent has evolved to handle data from a wide range of sources, integrating seamlessly with other components of the portfolio optimization system.',
    allow_delegation = True,
    verbose = 2
)   

mutual_fund_data_task = Task(
    description = "Search the internet for real-time data on domestic and international mutual funds."
            "Collect data exclusively for the current date to ensure relevance."
            "Aggregate and format the collected data for use in portfolio optimization."
            "Ensure data accuracy and completeness by cross-referencing multiple sources.",
    expected_output = "The expected output of the Mutual Fund Data Collector Agent is a structured dataset containing:"
            "Real-time mutual fund prices and NAVs for domestic and international markets"
            "Yields, holdings, and other relevant metrics of the mutual funds."
            "A timestamp indicating the collection date (current date)."
            "Metadata detailing the sources of the data collected.",
    tools = [exa_tool]
)




