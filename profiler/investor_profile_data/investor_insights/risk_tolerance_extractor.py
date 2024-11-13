from steps.chat_with_openai import ChatWithAI


class RiskToleranceAugment:
    """
    A class to extract risk tolerance data from an investor profile.
    """
    def __init__(self, risk_tolerance_data: str, liquidity_needs_data: str, api_key: str):
        self.__risk_tolerance_data = risk_tolerance_data
        self.__liquidity_needs_data = liquidity_needs_data
        self.__api_key = api_key
    

    def augment_data(self): 
        """
        Augments the risk tolerance data using a large language model (LLM).
        """
        # Prompt
        prompt = f"""Augment the following risk tolerance content to 60 to 100 words writing about the risk tolerance of the investor.
        Make sure not to add too much extra information and try to write using the given context only.
        Use an elaborative tone to rewrite this para.\ncontent: {self.__risk_tolerance_data}.
        Also take in consideration these liquidity needs of the investor: {self.__liquidity_needs_data}"""

        chat = ChatWithAI(prompt, self.__api_key)

        response = chat.get_response_from_llm()
        return response

