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



class OtherInfo(base):
    """  
    Class to store other information of an investor

    Arguments:
        tax_consideration: str: Tax consideration of the investor
        estate_plan: str: Estate plan of the investor
        insurance: str: Insurance of the investor
        other: str: Other information of the investor
    
    Returns:
        str: A string representation of the class object
    """ 
    def __init__(self, tax_consideration: str = None, estate_plan: str = None, insurance: str = None, other: str = None): 
        self.__tax_consideration = tax_consideration
        self.__estate_plan = estate_plan
        self.__insurance = insurance
        self.__other = other


    def __str__(self):
        other_info = [] # List 

        if self.__tax_consideration:
            other_info.append(f"Tax Consideration: {self.__tax_consideration}")
        if self.__estate_plan:
            other_info.append(f"Estate Plan: {self.__estate_plan}")
        if self.__insurance:
            other_info.append(f"Insurance: {self.__insurance}")
        if self.__other:
            other_info.append(f"Other: {self.__other}")

        return "\n".join(other_info)


    # Getters
    def get_tax_consideration(self):
        return self.__tax_consideration

    def get_estate_plan(self):
        return self.__estate_plan

    def get_insurance(self):
        return self.__insurance
    
    def get_other(self):
        return self.__other
    
