# Script for data pipeline of various assets, outputs the final data as json format to the knowledge_base dir 
from abc import ABC, abstractmethod
from steps.chat_with_openai import ChatWithAI
import uuid
import datetime
import json
import os


class Base(ABC):
    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass


class AssetETL(Base): 
    def __init__(self, destination: str, asset_type: str):
        self.destination = destination
        self.asset_type = asset_type 


    def extract(self, asset_data: str):
        """ 
        This method extracts data from the source, be it agents or apis

        Arguments
            - asset_data: A string type, para which contain all information about the specified asset 
        Returns 
            - inits data for the current object instance
        """
        if len(asset_data) < 200 or len(asset_data) > 5000:
            raise ValueError("[failed] Data is either too short or too long")
        else:
            self.data = asset_data
            print("[done] --Data extraction success--")


    def transform(self, api_key: str):
        """ 
        This method transforms data to fix inconsistency or abnormality 
        """
        ### Basic Preprocessing 
        try: 
            self.data = self.data.lower() # lower casing

            self.data = self.data.strip().replace("  ", " ")

            # Summarize using open ai for exceeding certain length 
            if len(self.data.split()) > 2500:
                prompt = "Summarize the following text to 2500 words or close:\n" + self.data
                
                # LLM 
                llm = ChatWithAI(prompt, api_key)
                self.data = llm.get_response_from_llm()
            
            print("[done] --Data transformation success--")

        except Exception as e:
            print(f"[failed] {e}")


    def load(self):
        """This method saves the transformed data into a json file in the output dir"""
        # text 
        unique_id = str(uuid.uuid4())
        data = {
            "unique_id": unique_id,
            "data": self.data,
            "asset_type": self.asset_type,
            "date": str(datetime.datetime.now())[:19]
        }
        
        # define path
        path = os.path.join(self.destination, f"{self.asset_type}")
        # create path if not exists
        if not os.path.exists(path):
            os.makedirs(path)
            print("dir Created")

        # file name
        name = f"{self.asset_type}_{str(datetime.date.today()).replace('-', '_')}_{unique_id[:8]}.json"

        try:
            # Dump to json
            with open(os.path.join(path, name), 'w') as f:
                json.dump(data, f, indent=4)
                print("[done] --Data load success--")

        except Exception as e: 
            print(f"[failed] {e}")

        