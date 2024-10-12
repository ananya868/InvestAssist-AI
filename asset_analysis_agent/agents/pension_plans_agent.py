from abc import ABC, abstractmethod
from crewai import Agent



# Define the Agent Interface
class AgentBase(ABC):
    """ 
    Base class for defining Agent Classes 
    """
    @abstractmethod 
    def build_agent(self):
        pass


# Define the PensionPlans Agent
class PensionPlansAgent(AgentBase):
    """ 
    This class instantiates the PensionPlans Agent Class

    Attributes: 
        role: Role of the agent (One line) 
        goal: Goal of the agent (Few lines)
        backstory: Backstory of the Agent (Para)

    Methods:
        build_agent: Builds the Agent Object with the given attributes
            **kwargs: A dictionary containing the other parameters that the Agent object might require 

        returns: 
            PensionPlans Agent Object
    """
    def __init__(self, role, goal, backstory):
        # Initialize the PensionPlans Agent with the given attributes
        self.role = role
        self.goal = goal
        self.backstory = backstory


    def build_agent(self, **kwargs):
        # Build the PensionPlans Agent Object with the given attributes and other parameters
        agent_attributes = {
            'role': self.role,
            'goal': self.goal,
            'backstory': self.backstory,
            'allow_delegation': True,
        }

        # Updates the other parameters if not None
        agent_attributes.update(kwargs)
        
        # Return the Agent object 
        return Agent(  
            **agent_attributes
        )
    


