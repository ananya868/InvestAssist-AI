# Takes in raw input data and extend it without adding information using LLM
from chat_with_openai import ChatWithAI


class CurrentPortfolioAssessmentAugment:
    """
    A class to extract current portfolio data from an investor profile.
    """
    def __init__(self, basic_info: str, historical_investment_data: str, api_key: str):
        self.__basic_info = basic_info
        self.__historical_investment_data = historical_investment_data
        self.__api_key = api_key
    

    def augment_data(self): 
        """
        Augments the current portfolio data using a large language model (LLM).
        """
        # Prompt
        prompt = f"""Augment the following content to 80 to 120 words writing about the current portfolio of the investor.
        Make sure not to add too much extra information and try to write using the given context only.
        Use an elaborative tone to rewrite this para.\nContent: {self.__basic_info}.
        Historical investments made by investor : {self.__historical_investment_data}."""

        chat = ChatWithAI(prompt, self.__api_key)

        response = chat.get_response_from_llm()
        return response





