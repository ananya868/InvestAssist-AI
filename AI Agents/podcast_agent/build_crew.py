import crewai 
from crewai import Crew


class PodcastCrew: 
    def __init__(self, agents: list, tasks: list, verbose: bool=True):
        self.agents = agents
        self.tasks = tasks
        self.verbose = verbose
    

    def build(self):
        crew = Crew(agents=self.agents, tasks=self.tasks, verbose=self.verbose)
        return crew 



