from abc import ABC, abstractmethod


class base(ABC):
    """
    Base abstract class for Financial Goals class
    """
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        pass


class FinancialGoals(base):
    """
    Class to store financial goals of an investor

    Arguments:
        primary_goal: str: Primary financial goal of the investor
        secondary_goal: str: Secondary financial goal of the investor

    Returns:
        str: A string representation of the class object 
    """
    def __init__(self, primary_goal: str, secondary_goal: str): 
        self.__primary_goal = primary_goal # Str
        self.__secondary_goal = secondary_goal # Str

    
    def __str__(self):
            return f"Primary Goal: {self.__primary_goal}\nSecondary Goal: {self.__secondary_goal}"

    
    # Getters 
    def get_primary_goal(self): 
        return self.__primary_goal
    
    def get_secondary_goal(self):
        return self.__secondary_goal





