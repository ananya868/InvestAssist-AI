from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import os 

def separate_fields(data_dict: dict):
    """Separate fields into different dictionaries based on their types."""

    text_list = []
    for k, v in data_dict.items():
        if isinstance(v, str):
            text_list.append(
                {'text': v, 'instrument_name': k}
            )
        else:
            print(f"Field {k} is not a string. Skipping...")

    return text_list

