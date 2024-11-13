# Takes in raw input data and extend it without adding information using LLM
from steps.chat_with_openai import ChatWithAI


class FinancialGoalsAugment:
    """
    A class to extract Financial goals data from an investor profile.
    """
    def __init__(self, financial_goals_data: str, investment_preference_data: str, api_key: str):
        self.__financial_goals_data = financial_goals_data 
        self.__investment_preference_data = investment_preference_data
        self.__api_key = api_key
    

    def augment_data(self): 
        """
        Augments the risk financial goals data using a large language model (LLM).
        """
        # Prompt
        prompt = f"""Augment the following content to 60 to 100 words writing about the financial goals of the investor.
        Make sure not to add too much extra information and try to write using the given context only.
        Use an elaborative tone to rewrite this para.\nContent: {self.__financial_goals_data}.
        Also take in consideration the investment preferences : {self.__investment_preference_data}."""

        chat = ChatWithAI(prompt, self.__api_key)

        response = chat.get_response_from_llm()
        return response




