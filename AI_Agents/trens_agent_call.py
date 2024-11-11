from markets_trend_agent.agents.custom_agent import CustomAgent 
from markets_trend_agent.tasks.custom_task import CustomTask 
from markets_trend_agent.tools.exa_tool import EXATool
from crewai import Crew

import json
import os

# Market trends agent, news agent, social media agent 



def MarketsTrendAgent(agent_list: list=['all'], llm_model: str='gpt-3.5-turbo'):
    """
    This function runs the Market Trends AI agent to generate real-time market trends data from the internet!
    It runs crew ai agents taking certain prompts, you might tune these prompts according to your needs.
    Args:
        agent_list (list): A list of agents to run the analysis. Default is ['all']. Otherwise, provide a list of specific agents to run.
        llm_model (str): The LLM model to use for the analysis. Default is 'gpt-3.5-turbo'.
    Returns:
        final_output (dict): A dictionary containing the final output from the agents in a dictionary format. 
    """  
    tools = [EXATool.build_tool()]
    params = {'tools': tools, 'LLM': llm_model}

    # prompts from json
    try:
        with open('prompts/market_agent_prompts.json') as f:
            agent_prompts = json.load(f)
        with open('prompts/market_task_prompts.json') as f:
            task_prompts = json.load(f)
        print("[INFO] --json loaded successfully!--")
    except Exception as e:
        print(f"[ERROR] --json loading failed!-- {e}")
    
    # check if agent_list is empty using assert
    assert len(agent_list) > 0, 'Please provide a list of assets to analyze!.'

    # agents
    if 'all' not in agent_list:
        agents = {k:v for k, v in prompts.items() if k in agent_list}
        tasks = {k:v for k, v in task_prompts.items() if k in agent_list}
    else:
        agents = agent_prompts
        tasks = task_prompts
    
    # AI Agent creation
    final_output = {} # final output dictionary
    for agent_name, prompts in agents.items():
        # Crew ai agent 
        agent = CustomAgent(
            role=prompts.get('role'),
            goal=prompts.get('goal'),
            backstory=prompts.get('backstory')
        ).build_agent(**params)

        # Crew ai task
        task = CustomTask(
            description=tasks.get(agent_name).get('description'),
            expected_output=tasks.get(agent_name).get('expected_output'),
            tools=tools,
            agent=agent
        ).build_task()

        # Crew ai Crew
        try:
            crew = Crew(agents=[agent], tasks=[task])
            print(f"[INFO] --{agent_name} agent created successfully!--")
        except Exception as e:
            print(f"[ERROR] --{agent_name} agent creation failed!-- {e}")
        
        # Run the crew
        output = crew.kickoff() # pass inputs if req
        # ... 
        final_output[agent_name] = output

    return final_output
    
