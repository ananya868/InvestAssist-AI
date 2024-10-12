from abc import ABC, abstractmethod



class base(ABC):
    """
    Base class for historical investment behavior data
    """
    @abstractmethod
    def __init__(self):
        pass 

    def __str__(self): 
        pass



class HistoricalInvestmentBehavior(base):
    """
    Class to store historical investment behavior data of an investor

    Arguments:
        previous_investment: str: Previous investment of the investor
        performance: str: Performance of the investor
    
    Returns:
        str: A string representation of the class object
    """
    def __init__(self, previous_investment: str, performance: str):
        self.__previous_investment = previous_investment
        self.__performance = performance
    

    def __str__(self):
        return f"Previous Investment: {self.__previous_investment}\nPerformance: {self.__performance}"


    # Getters 
    def get_previous_investment(self):
        return self.__previous_investment
    
    def get_performance(self):
        return self.__performance 

