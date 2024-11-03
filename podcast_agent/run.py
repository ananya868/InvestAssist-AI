import warnings 
# ignore warnings
warnings.filterwarnings("ignore")

from podcast_data_agent import PodcastDataAgent
from podcast_data_task import PodcastDataTask
from build_crew import PodcastCrew
from crewai_tools import YoutubeVideoSearchTool, YoutubeChannelSearchTool
import os 
from dotenv import load_dotenv
load_dotenv()

# Example usage
# For agent 1
a1_role = "Youtube Video transcripts data collector"
a1_goal = "Search Youtube and collect video transcripts based on query given"
a1_verbose = True
a1_backstory = """You excel at searching Youtube for videos and collecting their transcripts.
                You make sure that you collect the most relevant information.
                Make sure that the transcriptions align with the query given"""

# For agent 2
a2_role = "Transcription data formatter"
a2_goal = "Formats the transcriptions data in a specified format"
a2_verbose = False 
a2_backstory = """Your job is to format the transcriptions data from the previous agent.
                The instructions to format the transcriptions data are:.
                Rewrite the content to a markdown format.
                Use headings and subheadings as required.   
                Make bullet points as required"""


# Tasks 
# For agent 1 
t1_description = "Go through various youtube videos to collect transcriptions. The video topic is: real estate investment in 2024"
t1_expected_output = "a comprehensive list of youtube videos transcriptions. the final output should be 2000 words, containing data of video transcriptions"
t1_human_input = False 
# t1_agent 

# For agent 2 
t2_description = "Format the data according to the instructions provided"
t2_expected_output = "a markdown formatted article containing the video transcriptions insights"
t2_human_input = False 
# t2_agent

# youtube tool 
video_url = "https://www.youtube.com/watch?v=fUtDU0U7Zqw"
# Build the crew 
# lets create agents
# try:
data_collector_agent = PodcastDataAgent(agent_role=a1_role, agent_goal=a1_goal, verbose=a1_verbose, backstory=a1_backstory, tools=[YoutubeVideoSearchTool(video_url)])
agent1 = data_collector_agent.build()
data_formatter_agent = PodcastDataAgent(agent_role=a2_role, agent_goal=a2_goal, verbose=a2_verbose, backstory=a2_backstory)
agent2 = data_formatter_agent.build()

# tasks 
data_collector_task = PodcastDataTask(description=t1_description, expected_output=t1_expected_output, agent=agent1, human_input=t1_human_input)
task1 = data_collector_task.build()  
data_formatter_task = PodcastDataTask(description=t2_description, expected_output=t2_expected_output, agent=agent2, human_input=t2_human_input)
task2 = data_formatter_task.build()
print(f"agents and tasks initiated")
# --works till here--

# build the crew
cr = PodcastCrew(agents=[agent1, agent2], tasks=[task1, task2], verbose=True)
crew = cr.build()
print("[done] --Crew built successfully--")
# print(type(crew))

# run the crew
# input_data = {"query": "real estate investment in 2024"}
result = crew.kickoff()
print(f"[done] --Crew run successfully--")

# save the result
print(type(result))
# save the result using with open
with open("result.txt", "w") as f:
    f.write(result)
    print("[done] --Result saved successfully--")

# except Exception as e:
    print(f"Error building the crew: {e}")

