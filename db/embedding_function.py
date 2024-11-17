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


def generate_embedding(text_list: list[dict]):
    # Initialize a Pinecone client with your API key
    pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))

    # Convert the text into numerical vectors that Pinecone can index
    embeddings = pc.inference.embed(
        model="multilingual-e5-large",
        inputs=[d['text'] for d in text_list],
        parameters={"input_type": "passage", "truncate": "END"}
    )

    return embeddings.data # list[dict] of embeddings