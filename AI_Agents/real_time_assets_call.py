from AI_Agents.asset_analysis_agent.agents.custom_agent import CustomAgent
from AI_Agents.asset_analysis_agent.tasks.custom_task import CustomTask
from AI_Agents.asset_analysis_agent.tools.exa_tool import EXATool

import json 
import os 

from crewai import Crew 



def real_time_assets_agent(run: str='all', llm_model: str='gpt-3.5-turbo'):

    tools = [EXATool().build_tool()]
    params = {'tools': tools, 'LLM': llm_model}

    # Prompts from json 
    try:
        with open('AI_Agents/prompts/real_time_asset_prompts.json', 'r') as f:
            agent_prompts = json.load(f)
        with open('AI_Agents/prompts/real_time_asset_task_prompts.json', 'r') as f:
            task_prompts = json.load(f)
        print("[INFO] --json loaded successfully!--")
    except Exception as e:
        print(f"[ERROR] --json loading failed!-- {e}")
    

    if run == 'all': 
        agents = agent_prompts
        tasks = task_prompts
    
    # AI Agent creation
    final_output = {} # final output dictionary
    for agent_name, prompt in agents.items():
        # Crew ai Agent
        agent = CustomAgent(
            role=prompt.get('role'),
            goal=prompt.get('goal'),
            backstory=prompt.get('backstory')
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
        output = crew.kickoff()
        
        final_output[agent_name] = output

    return final_output
    