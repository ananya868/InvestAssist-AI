from AI_Agents.asset_analysis_agent.agents.custom_agent import CustomAgent
from AI_Agents.asset_analysis_agent.tasks.custom_task import CustomTask
from AI_Agents.asset_analysis_agent.tools.exa_tool import EXATool

import json 
import os 

from crewai import Crew




def AssetAnalysisAgent(agent_list: list=['all'], llm_model: str='gpt-3.5-turbo'):
    """  
    This function runs the Asset Analysis AI agent to generate real-time assets data from the internet!
    It runs crew ai agents taking certain prompts, you might tune these prompts according to your needs.
    
    Args:
        agent_list (list): A list of agents to run the analysis. Default is ['all']. Otherwise, provide a list of specific agents to run.
        llm_model (str): The LLM model to use for the analysis. Default is 'gpt-3.5-turbo'.
    Returns:
        final_output (dict): A dictionary containing the final output from the agents in a dictionary format. 
    """  
    # params 
    tools = [EXATool.build_tool()]
    params = {'tools': tools, 'LLM': llm_model}

    # prompts from json 
    try:
        with open('prompts/asset_agent_prompts.json', 'r') as f:
            agent_prompts = json.load(f)
        with open('prompts/asset_task_prompts.json', 'r') as f:
            task_prompts = json.load(f)
        print("    [info] --assets prompts loaded successfully!--")
    except Exception as e:
        print(f"    [error] --assets prompts loading failed!-- {e}")

    # check if agent_list is empty using assert 
    assert len(agent_list) > 0, 'Please provide a list of assets to analyze!.'

    # agents
    if 'all' not in agent_list:
        agents = {k:v for k, v in agent_prompts.items() if k in agent_list}
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
            print(f"    [info] --{agent_name} agent created successfully!--")
        except Exception as e:
            print(f"    [error] --{agent_name} agent creation failed!-- {e}")

        # run the crew
        output = crew.kickoff() # pass inputs if req
        # ....
        final_output[agent_name] = output
    
    return final_output # dict 
    


# Sample output 

# {
#     "stocks": "Last week stocks rose by 20%, while the cryptocurrency market gained 15%.....",
#     "cryptocurrency": "The cryptocurrency market has been on a bullish run for the past few days....",
#     # ..... 
# }

    