from abc import ABC, abstractmethod



class base(ABC):
    """
    Base class for Risk tolerance data
    """
    @abstractmethod
    def __init__(self):
        pass 

    def __str__(self): 
        pass



class RiskTolerance(base): 
    """
    Class to store risk tolerance data of an investor

    Arguments:
        risk_assessment: str: Risk assessment of the investor
        details: str: Details of the risk assessment
    
    Returns:
        str: A string representation of the class object
    """
    def __init__(self, risk_assessment: str, details: str):
        self.__risk_assessment = risk_assessment
        self.__details = details 
    

    def __str__(self):
        return f"Risk Assessment: {self.__risk_assessment}\nDetails: {self.__details}"


    # Getters
    def get_risk_assessment(self):
        return self.__risk_assessment
    
    def get_details(self):
        return self.__details



