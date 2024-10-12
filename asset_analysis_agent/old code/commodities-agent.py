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


commodities_data_agent = Agent(
    role = 'commodities Data Collector', 
    goal = 'The primary goal of the Commodities Data Collector Agent is to gather real-time data on commodities, such as metals and energy,'
            'from domestic and international markets for the current date, providing accurate and comprehensive information to be used in investor portfolio optimization.',
    backstory = 'The Commodities Data Collector Agent was developed to meet the increasing need for timely and accurate data on commodities markets, which are crucial components of diversified investment portfolios.'
            'Investors require up-to-date information on prices, trends, and market conditions for metals and energy commodities to make informed decisions.'
            'This agent was created to automate the process of data collection, ensuring that investors have access to the most current and comprehensive commodities information.'
            'Over time, the agent has evolved to handle data from a wide range of sources, integrating seamlessly with other components of the portfolio optimization system.',
    allow_delegation = True,
    verbose = 2
)   

commodities_data_task = Task(
    description = "Search the internet for real-time data on domestic and international commodities, including metals and energy."
            "Collect data exclusively for the current date to ensure relevance."
            "Aggregate and format the collected data for use in portfolio optimization."
            "Ensure data accuracy and completeness by cross-referencing multiple sources.",
    expected_output = "The expected output of the Bond Data Collector Agent is a structured dataset containing:"
            "Real-time bond prices for domestic and international markets."
            "Yields, maturities, and ratings of the bonds."
            "Relevant bond metrics and indicators."
            "A timestamp indicating the collection date (current date)."
            "Metadata detailing the sources of the data collected.",
    tools = [exa_tool]
)




