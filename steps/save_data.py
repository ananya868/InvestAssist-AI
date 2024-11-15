# Script for data pipeline of various data strings, outputs the final data as json format to the knowledge_base dir 
from abc import ABC, abstractmethod
import uuid
import datetime
import json
import os


class Base(ABC):
    @abstractmethod
    def check(self):
        pass 

    @abstractmethod
    def save(self):
        pass


class SaveData(Base): 
    def __init__(self, destination: str, data_field: str):
        self.destination = destination
        self.type = data_field 


    def check(self, data: str):
        """ 
        This method extracts data from the source, be it agents or apis

        Arguments
            - data: A string type, para which contain all information about the specified asset 
        Returns 
            - inits data for the current object instance
        """
        if len(data.split()) < 200 or len(data.split()) > 1000:
            raise ValueError("[failed] Data is either too short or too long")
        else:
            self.data = data
            # print("[done] --Data Checked success--")
        
        return self.data

    def save(self):
        """This method saves the transformed data into a json file in the output dir"""
        # text 
        unique_id = str(uuid.uuid4())
        json_data = {
            "unique_id": unique_id,
            "data": self.data,
            "type": self.type,
            "date": str(datetime.datetime.now())[:19]
        }
        
        # define path
        path = os.path.join(self.destination, f"{self.type}")
        # create path if not exists
        if not os.path.exists(path):
            os.makedirs(path)
            print("dir Created")

        # file name
        name = f"{self.type}_{str(datetime.date.today()).replace('-', '_')}_{unique_id[:8]}.json"

        try:
            # Dump to json
            with open(os.path.join(path, name), 'w') as f:
                json.dump(json_data, f, indent=4)
                # print("[done] --Data Saved Successfully--")

        except Exception as e: 
            print(f"    [failed] {e}")

        return json_data
        