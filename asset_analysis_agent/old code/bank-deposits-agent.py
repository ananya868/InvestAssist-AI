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


bank_deposit_data_agent = Agent(
    role = 'Bank Deposits Data Collector', 
    goal = 'The Bank Deposit Data Collector Agent is responsible for searching the internet for real-time data on bank deposits in the domestic market. '
            'It focuses exclusively on collecting data for the current date, ensuring that all information is current and accurate. '
            'The collected data includes various bank deposit schemes and other relevant details, which are essential for optimizing investors portfolios',
    backstory = 'The Bank Deposit Data Collector Agent was developed to meet the growing demand for timely and accurate data on bank deposit schemes, which are an important component of low-risk investment portfolios.'
            'Investors need up-to-date information on interest rates, terms, and conditions of various bank deposit schemes to make informed decisions.'
            'This agent was created to automate the process of data collection, ensuring that investors can access the most current and comprehensive information.'
            'Over time, the agent has evolved to handle data from a wide range of sources, integrating seamlessly with other components of the portfolio optimization system',
    allow_delegation = True,
    verbose = 2
)   

bank_deposit_data_task = Task(
    description = "Search the internet for real-time data on domestic bank deposits."
            "Collect data exclusively for the current date to ensure relevance."
            "Aggregate and format the collected data for use in portfolio optimization."
            "Ensure data accuracy and completeness by cross-referencing multiple sources", 
    expected_output = "The expected output of the Bank Deposit Data Collector Agent is a structured dataset containing:"
            "Real-time interest rates for domestic bank deposits."
            "Terms, conditions, and other details of various bank deposit schemes."
            "A timestamp indicating the collection date (current date)."
            "Metadata detailing the sources of the data collected.",
    tools = [exa_tool]
)




