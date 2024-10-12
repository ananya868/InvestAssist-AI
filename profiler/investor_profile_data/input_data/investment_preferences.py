from abc import ABC, abstractmethod



class base(ABC):
    """
    Base class for investment preferences data
    """
    @abstractmethod
    def __init__(self):
        pass 

    def __str__(self): 
        pass



class InvestmentPreferences(base):
    """
    Class to store investment preferences data of an investor
    
    Arguments:
        asset_preference: str: Asset preference of the investor
        sector_preference: str: Sector preference of the investor
        geographic_preferences: str: Geographic preferences of the investor
        ethical_consideration: str: Ethical considerations of the investor
    
    Returns:
        str: A string representation of the class object
    """
    def __init__(self, asset_preference: str, sector_preference: str = None, geographic_preferences: str = None, ethical_consideration: str = None):
        self.__asset_preference = asset_preference
        # Optional 
        self.__sector_preference = sector_preference
        self.__geographic_preferences = geographic_preferences
        self.__ethical_consideration = ethical_consideration

    
    def __str__(self):
        preferences = []
        preferences.append(f"Asset Preference: {self.__asset_preference}") # Mandatory
        
        # optional
        if self.__sector_preference:
            preferences.append(f"Sector Preference: {self.__sector_preference}") 
        if self.__geographic_preferences:
            preferences.append(f"Geographic Preferences: {self.__geographic_preferences}")
        if self.__ethical_consideration:
            preferences.append(f"Ethical Consideration: {self.__ethical_consideration}")
        
        return "\n".join(preferences)

    
    # Getters
    def get_asset_preference(self):
        return self.__asset_preference
    
    def get_sector_preference(self):
        return self.__sector_preference 
    
    def get_geographic_preferences(self):   
        return self.__geographic_preferences

    def get_ethical_consideration(self):
        return self.__ethical_consideration 


