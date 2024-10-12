from abc import ABC, abstractmethod
from crewai import Task 



# Define the Task Interface 
class TaskBase(ABC):
    """
    Base class for defining Task classes
    """  
    @abstractmethod
    def build_task(self):
        pass



class BondsTask(TaskBase): 
    """
    This class instantiates the Bonds Task Class

    Attributes: 
        description: A description of the task (Para)
        expected_output: The expected output of the task (Para)
        tools: A list of tools required for the task
        agent: The agent responsible for the task

    Methods:
        build_task: Builds the Task Object with the given attributes
            **kwargs: A dictionary containing the other parameters that the Task object might require 

        returns: 
            Bonds Task Object 
    """
    def __init__(self, description, expected_output, tools, agent):
        # Initialize the Bonds Task with the given attributes
        self.description = description
        self.expected_output = expected_output
        self.tools = tools
        self.agent = agent

    def build_task(self, **kwargs):
        # Build the Bonds Task Object with the given attributes and other parameters
        task_attributes = {
            'description': self.description,
            'expected_output': self.expected_output,
            'tools': self.tools,
            'agent': self.agent,
        }

        # Updates the other parameters if not None
        task_attributes.update(kwargs)

        # Return the Task object 
        try:
            return Task(  
                **task_attributes
            )
        except:
            return "Failed to build Bonds Task!"