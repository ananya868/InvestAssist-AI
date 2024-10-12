# script that takes in raw strings and combine them to form json files 
import json
import os 



class BuildJson: 
    """  
    Takes in string values, combine them and saves json with the name of the investor  
    """
    def __init__(self, basic_info: str, financial_goals: str, risk_tolerance: str, historical_investments: str, 
                    investment_horizon: str, investment_preferences: str, liquidity_needs: str, other_info: str):
        self.__basic_info = basic_info
        self.__financial_goals = financial_goals
        self.__risk_tolerance = risk_tolerance
        self.__historical_investments = historical_investments
        self.__investment_horizon = investment_horizon
        self.__investment_preferences = investment_preferences
        self.__liquidity_needs = liquidity_needs
        self.__other_info = other_info
        self.__json_data = {}

    def build_json(self):
        """
        Builds json from the given strings
        """
        try:
            self.__json_data = {
                "basic_info": self.__basic_info,
                "financial_goals": self.__financial_goals,
                "risk_tolerance": self.__risk_tolerance,
                "historical_investments": self.__historical_investments,
                "investment_horizon": self.__investment_horizon,
                "investment_preferences": self.__investment_preferences,
                "liquidity_needs": self.__liquidity_needs,
                "other_info": self.__other_info
            }

            return self.__json_data
        except Exception as e:
            print(e)

    def get_name(self):
        """
        Returns the name of the investor
        """
        name = self.__basic_info.split("Name:")
        return name[1].split('\nAge')[0].replace(" ", "")
    
    def save_json(self):
        """
        Saves the json data to a file
        """
        try:
            # make dir if not exist
            save_dir = os.path.join(os.getcwd(), 'profiler\\' 'json_profiles') ### Highly experimental 
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            with open(os.path.join(save_dir, f"{self.get_name()}_profile.json"), "w") as f:
                json.dump(self.__json_data, f, indent=4)
        except Exception as e:
            print(e)