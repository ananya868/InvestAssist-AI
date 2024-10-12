from abc import ABC, abstractmethod



class base(ABC):
    """
    Base class for Liquidity Needs data
    """
    @abstractmethod
    def __init__(self):
        pass 

    def __str__(self): 
        pass



class LiquidityNeeds(base): 
    """
    Class to store liquidity needs data of an investor

    Arguments:
        emergency_funds: str: Emergency funds of the investor
        other: str: Other liquidity needs of the investor
    
    Returns:
        str: A string representation of the class object
    """ 
    def __init__(self, emergency_funds: str = None, other: str = None): 
        self.__emergency_funds = emergency_funds
        self.__other = other
    

    def __str__(self):
        liquidity_needs = []

        if self.__emergency_funds:
            liquidity_needs.append(f"Emergency funds: {self.__emergency_funds}") 
        if self.__other:
            liquidity_needs.append(f"Other needs: {self.__other}")

        return "\n".join(liquidity_needs)

    
    # Getters
    def get_emergency_funds(self):
        return self.__emergency_funds
    
    def get_other(self):
        return self.__other 
