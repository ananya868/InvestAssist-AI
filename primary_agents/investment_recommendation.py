# Script to define investment recommendation agent 
# - recommends investment by analyzing the assets and market trend data, real time 
# - uses LLM model to generate tailored investment recommendations


class InvestmentRecommenderAgent:
    def __init__(self, current_portfolio: str, financial_goals: str, summarized_asset_data: str, trends_data: str, api_key: str, model: str = 'gpt-3.5-turbo'): 
        self.__current_portfolio = current_portfolio
        self.__financial_goals = financial_goals
        self.__summarized_asset_data = summarized_asset_data
        self.__trends_data = trends_data
        self.__api_key = api_key
        self.model = model

    
    def generate_recommendation(self):
        """
        Generates a tailored investment recommendation based on the user's investment portfolio and market data.
        """
        # Prompt
        prompt = f"""You are a financial analyst and your job is to analyze the investor current portfolio and generate an investment recommendation after analyzing the insights from the market data that is provided to you.
            Write a 200 words investment recommendation for the investor based on the following information:
            Current Portfolio of the investor: {self.__current_portfolio}.
            Financial Goals: {self.__financial_goals}.
            Market Data: latest assets data: {self.__summarized_asset_data}.
            Latest trends in the market data: {self.__trends_data}"""

        # Chat with AI
        chat = ChatWithAI(prompt, self.__api_key, self.model)
        response = chat.get_response_from_llm()
        
        return response


    def format(self, recommendation: str):
        """
        Formats the recommendation and saves it to a file.
        """
        # Format the recommendation
        prompt = f"""You are a formatter agent, whose job is to take in raw document/text data and properly format it to markdown format as per instructions: 
            - The title of the document should be "Investment Recommendation".
            - There should be sub-headings where ever you feel necessary 
            - analyse and make important recommendation words as bold
            - The recommendation should be in bullet points.

            Here is the recommendation that needs to be formatted:
            {recommendation}"""

        
        # Chat with AI
        chat = ChatWithAI(prompt, self.__api_key, self.model)
        response = chat.get_response_from_llm()

        return response

    
    def save(self, markdown_content: str, directory='output\investment_recommendations'):
        """
        Creates a new file with a sequential number in the filename.
        """
        base_name = 'recommendation'
        os.makedirs(directory, exist_ok=True) # make dir if not exist
        files = os.listdir(directory) 
        similar_files = [f for f in files if f.startswith(base_name)]
        
        # Extract numbers from filenames and find the highest
        max_number = 0
        for file_name in similar_files:
            try:
                number_part = int(file_name.split('_')[-1].split('.')[0])
                if number_part > max_number:
                    max_number = number_part
            except ValueError:
                continue
        
        # New filename with the next number in sequence
        new_number = max_number + 1
        new_file_name = f"{base_name}_{new_number}.md"
        new_file_path = os.path.join(directory, new_file_name)
    
        with open(new_file_path, "w") as file:
            file.write(markdown_content)
            # print("Saved the markdown file!")




