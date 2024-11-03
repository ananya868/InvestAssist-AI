from crewai import Agent
from abc import ABC, abstractmethod


class AgentBase(ABC):
    @abstractmethod
    def __init__(self, agent_role, agent_goal, verbose:bool, backstory: str, tools: list=None):
        self.agent_role = agent_role
        self.agent_goal = agent_goal
        self.tools = tools
        self.verbose = verbose
        self.backstory = backstory

    @abstractmethod
    def build(self):
        pass


class PodcastDataAgent(AgentBase):
    def __init__(self, agent_role, agent_goal, verbose: bool, backstory: str, tools=None):
        super().__init__(agent_role, agent_goal, verbose, backstory, tools)

    def build(self):
        """
        Builds the crewai agent that collects data from the internet
        """
        # Create a crew
        try:
            agent = Agent(
                role=self.agent_role,
                goal=self.agent_goal,
                tools=self.tools,
                verbose=self.verbose,
                backstory=self.backstory
            )
            return agent
        except Exception as e:
            print(f"Error building agent object: {e}")




    

    
