import uuid 
import nanoid



class GenerateUID:
    def __init__(self):
        pass


    def generate_id(self):
        """  
        Generates unique id for individual data instances 
        """
        # uuid
        unique_id = nanoid.generate() 

        return unique_id
