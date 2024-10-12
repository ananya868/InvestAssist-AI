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


stock_data_agent = Agent(
    role = 'Stock Data Collector', 
    goal = 'The Stock Data Collector Agent is responsible for searching the internet for real-time data on stocks in both domestic and international markets.'
            ' It focuses exclusively on collecting data for the current date, ensuring that all information is up-to-date and relevant.'
            ' The gathered data is essential for optimizing investors portfolios',
    backstory = 'The Stock Data Collector Agent was conceived to address the increasing need for timely and accurate stock market data in portfolio optimization.'
            'In the fast-paced world of financial markets, having access to real-time data is crucial for making informed investment decisions. '
            'This agent was developed to automate the process of data collection, ensuring that investors have the most current stock information at their fingertips.'
            'Over time, the agent has evolved to handle a wide range of data sources, integrating seamlessly with other components of the portfolio optimization system.',
    allow_delegation = True,
    verbose = 2
)   

stock_data_task = Task(
    description = "Search the internet for real-time data on domestic and international stocks."
            "Collect data exclusively for the current date to ensure relevance."
            "Aggregate and format the collected data for use in portfolio optimization."
            "Ensure data accuracy and completeness by cross-referencing multiple sources.",
    expected_output = "The expected output of the Stock Data Collector Agent is a structured dataset containing." 
            "Real-time stock prices for domestic and international markets."
            "Trading volumes and market capitalizations."
            "Relevant stock metrics and indicators."
            "A timestamp indicating the collection date (current date)."
            "Metadata detailing the sources of the data collected.",
    tools = [exa_tool]
)

