from crewai import Task
from abc import ABC, abstractmethod


class TaskBase(ABC):
    @abstractmethod
    def __init__(self, description, expected_output, agent, human_input: bool=False):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent
        self.human_input = human_input

    @abstractmethod
    def build(self):
        pass


class PodcastDataTask(TaskBase):
    def __init__(self, description, expected_output, agent, human_input: bool=False):
        super().__init__(description, expected_output, agent, human_input)
    
    def build(self):
        """
        Builds the crewai agent that collects data from the internet
        """
        # Create a crew
        try:
            task = Task(
                description=self.description,
                expected_output=self.expected_output,
                agent=self.agent,
                human_input=self.human_input
            )
            return task

        except Exception as e:
            print(f"Error building task object: {e}")




    

    
