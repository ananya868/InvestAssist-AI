# Script to define the insights generator agent whose role is to generate insights on market data based on investor's preference


class InsightGeneratorAgent:
    def __init__(self, current_portfolio: str, summarized_asset_data: str, trends_data: str, api_key: str, model: str = 'gpt-3.5-turbo'): 
        self.__current_portfolio = current_portfolio
        self.__summarized_asset_data = summarized_asset_data
        self.__trends_data = trends_data
        self.__api_key = api_key
        self.model = model

    
    def generate_insights(self):
        """
        Generates insights on market data based on investor's preference.
        """
        # Prompt
        prompt = f"""You are a financial analyst and your job is to analyze the investor current portfolio and generate insights on those same assets that the investor have invested in by using the market data that is provided below:
            Current Portfolio: {self.__current_portfolio}.
            Market Data: latest assets data: {self.__summarized_asset_data}.
            Latest trends in the market data: {self.__trends_data}"""

        # Chat with AI
        chat = ChatWithAI(prompt, self.__api_key, self.model)
        response = chat.get_response_from_llm()
        
        return response
    

    def format(self, insights: str):
        """
        Formats the insights generated and saves it to a file.
        """
        # Format the insights
        prompt = f"""You are a formatter agent, whose job is to take in raw document/text data and properly format it to markdown format as per instructions: 
            - The title of the document should be "Market Insights".
            - There should be sub-headings where ever you feel necessary 
            - analyse and make important insights words as bold
            - The insights should be in bullet points.
        
            Here are the insights that need to be formatted:
            {insights}"""
        
        # Chat with AI
        chat = ChatWithAI(prompt, self.__api_key, self.model)
        response = chat.get_response_from_llm()

        return response
    

    def save(self, markdown_content: str, directory='output\market_insights'):
        """
        Creates a new file with a sequential number in the filename.
        """
        base_name = 'insight'
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


