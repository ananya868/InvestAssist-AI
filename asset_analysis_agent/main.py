from agents import stocks_agent 
from tasks import stocks_task
from dotenv import load_dotenv 
load_dotenv()


from crewai_tools import EXASearchTool

# Initialize the tool for internet searching capabilities
exa_tool = EXASearchTool()

role = 'gay' 
goal = 'hi'
backstory = 'bla bla'

tools = [exa_tool]


params = {'tools': tools, 'LLM': 'gpt-3.5-turbo'}
agent = stocks_agent.StockAgent(role, goal, backstory).build_agent(**params)

description = 'gggggggggggg'
expected_output = 'ahihfashfpa'

task = stocks_task.StocksTask(description, expected_output, tools, agent).build_task()
print(task)