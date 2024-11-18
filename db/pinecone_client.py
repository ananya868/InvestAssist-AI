import pinecone 
from pinecone import Pinecone, ServerlessSpec
import os
import shortuuid



def create_index(index_name, dimension, metric):
    # Create a new index with the specified name, dimension, and metric
    pc.create_index(
        name=index_name,
        dimension=1024, # your model dimension 
        metric="cosine", # your desired metric
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
    return pc 



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



def upsert_data(index_name: str, meta_data: list, embeddings: list):
    """Initialized a pinecone client that can be used to upsert data""" 
    pc = Pinecone(api_key=os.environ.get('PINECONE_API_KEY'))
    print('Client connected')

    # check if index already exists 
    flag = -1
    for items in pc.list_indexes().get('indexes'):
        if items.get('name') == index_name:
            print(f"Index {index_name} already exists, skipping creation!")
            flag = 1
            break 
    
    if flag == -1: 
        print(f"Index {index_name} does not exist. Creating index...")
        create_index(index_name, 1024, 'cosine')
        print(f"Index {index_name} created")

    # make our records to upsert 
    records = []
    for metadata, embedding in zip(meta_data, embeddings):
        records.append(
            {   
                'id': shortuuid.uuid(), # unique id for each record
                'values': embedding.get('values'),
                'metadata': {
                    'instrument_name': metadata['instrument_name'],
                    'text': metadata['text'],
                    },
            }
        )
    # upsert the records into the index 
    try:
        index = pc.Index(index_name)
        index.upsert(
            vectors=records
        )
        print(f"{len(records)} records Upserted")
    except Exception as e:
        print(f"Upsert failed: {e}")
