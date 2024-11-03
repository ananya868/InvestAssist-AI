# Script for data pipeline of various assets, outputs the final data as json format to the knowledge_base dir 
from abc import ABC, abstractmethod
from data_pipelines.chat_with_openai import ChatWithAI
import uuid
import datetime
import json
import os


class ProfilerBase:
    @abstractmethod
    def __init__(self):
        pass 

    def generate(self, data: json): 
        pass 


