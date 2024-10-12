from abc import ABC, abstractmethod



class base(ABC):
    """
    Base class for investment horizon data
    """
    @abstractmethod
    def __init__(self):
        pass 

    def __str__(self): 
        pass



class InvestmentHorizon(base):
    """
    Class to store investment horizon data of an investor

    Arguments:
        short_term: str: Short term investment horizon of the investor
        medium_term: str: Medium term investment horizon of the investor
        long_term: str: Long term investment horizon of the investor

    Returns:
        str: A string representation of the class object
    """
    def __init__(self, short_term:str=None, medium_term:str=None, long_term:str=None):
        self.__short_term = short_term
        self.__medium_term = medium_term
        self.__long_term = long_term


    def __str__(self):
        terms = [] # list for storing terms 
        if self.__short_term:
            terms.append(f"Short Term: {self.short_term}")
        if self.__medium_term:
            terms.append(f"Medium Term: {self.medium_term}")
        if self.__long_term:
            terms.append(f"Long Term: {self.long_term}")
        return "\n".join(terms)


    # Getters
    def get_short_term(self):
        return self.__short_term 
    
    def get_medium_term(self):
        return self.__medium_term
    
    def get_long_term(self):
        return self.__long_term
