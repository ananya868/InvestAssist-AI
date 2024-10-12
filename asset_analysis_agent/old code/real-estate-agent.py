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


real_estate_data_agent = Agent(
    role = 'Real Estate Data Collector', 
    goal = 'The Real Estate Data Collector Agent is responsible for searching the internet for real-time data on real estate in the domestic market. '
            'It focuses exclusively on collecting data for the current date, ensuring that all information is current and accurate. '
            'The collected data will be used for optimizing investors portfolios by providing insights into the real estate market.',
    backstory = 'The Real Estate Data Collector Agent was developed to meet the increasing need for timely and accurate data on the real estate market, a significant component of diversified investment portfolios.'
            'Investors require up-to-date information on property values, trends, and market conditions to make informed decisions. '
            'This agent was created to automate the process of data collection, ensuring that investors have access to the most current and comprehensive real estate information.'
            'Over time, the agent has evolved to handle data from a wide range of sources, integrating seamlessly with other components of the portfolio optimization system',
    allow_delegation = True,
    verbose = 2
)   

real_estate_data_task = Task(
    description = "Search the internet for real-time data on domestic real estate."
            "Collect data exclusively for the current date to ensure relevance."
            "Aggregate and format the collected data for use in portfolio optimization."
            "Ensure data accuracy and completeness by cross-referencing multiple sources.",
    expected_output = "The expected output of the Real Estate Data Collector Agent is a structured dataset containing:"
            "Real-time property values for the domestic real estate market."
            "Current market trends and conditions."
            "Relevant metrics and indicators for real estate."
            "A timestamp indicating the collection date (current date).",
    tools = [exa_tool]
)




