from abc import ABC, abstractmethod 



class base(ABC): 
    """ 
    Base abstract class for Basic Information class
    """
    @abstractmethod
    def __init__(self): 
        pass

    def __str__(self): 
        pass


class BasicInformation(base): 
    """
    Class to store basic information of an investor
    
    Arguments: 
        name: str: Name of the investor
        age: int: Age of the investor
        occupation: str: Occupation of the investor
        net_worth: float: Net worth of the investor

    Methods:
        __init__: Initializes the class object
        __str__: Returns a string representation of the class object
        get_name: Returns the name of the investor
        get_age: Returns the age of the investor
        get_occupation: Returns the occupation of the investor
        get_net_worth: Returns the net worth of the investor

    Returns:
        str: A string representation of the class object
    """

    def __init__(self, name: str, age: int, occupation: str, net_worth: float):
        self.__name = name # str
        self.__age = int(age)  # Ensure age is an integer
        self.__occupation = occupation # Str
        self.__net_worth = float(net_worth)  # Ensure net_worth is a float

    def __str__(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nOccupation: {self.__occupation}\nNet Worth: {self.__net_worth}"


    # Getters
    def get_name(self):
        return self.__name 

    def get_age(self): 
        return self.__age

    def get_occupation(self):
        return self.__occupation
    
    def get_net_worth(self): 
        return self.__net_worth 

 