import os 
from steps.chat_with_openai import ChatWithAI



class Summarizer:
    def __init__(self, text_list: list, sent_limit: int, api_key: str): 
        self.text_list = text_list
        self.sent_limit = sent_limit
        self.api_key = api_key
    
    
    def summarize(self): 
        """
        Summarizes a list of text using a large language model (LLM) using the OpenAI API.
        Primarily for summarizing long asset data, trends data into concise summaries for better analysis.
        """ 
        # Summarize each text in the list to the sent limit without losing important information 
        summarized_text_list = []
        for text in self.text_list:
            # Initialize the ChatWithAI class
            prompt = f"""
            Summarize the following text to {self.sent_limit} words without losing much information. 
            The text is information on financial assets (or trends), and need to be carefully summarized for better analysis.
            Make sure to include all key points and highlights.

            text: {text}
            """
            chat_with_ai = ChatWithAI(prompt=prompt, api_key=self.api_key)
            # Get the response from the LLM
            response = chat_with_ai.get_response_from_llm()
            summarized_text_list.append(response)

        # Combine the summarized text into a single string with a newline character between each text
        summarized_text = "\n".join(summarized_text_list)

        return summarized_text
        
