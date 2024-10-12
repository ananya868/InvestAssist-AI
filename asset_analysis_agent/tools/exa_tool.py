from abc import ABC, abstractmethod 
from crewai_tools import EXASearchTool



# Base Class for Tool interface 
class ToolBase(ABC):
    @abstractmethod 
    def build_tool(self): 
        pass



class EXATool(ToolBase):
    def build_tool(self): 
        try: 
            return EXASearchTool()
        except:
            print("Error: Unable to build EXASearchTool")
            return None
            




