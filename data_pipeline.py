# Script to run to update knowledge base with new data 
# CI/CD pipeline with Github Actions
# Important modules 
from steps.real_time_data_collection import real_time_data_collection_step
from db.helper_methods import separate_fields
from db.pinecone_client import generate_embedding, upsert_data



def update_data():
    # Step 1: Run AI-Agents
    assets_dict, trends_dict = real_time_data_collection_step()

    # Converting CrewAI Output to string
    assets_data = {}
    for k, v in assets_dict.items():
        assets_data[k] = v.raw

    trends_data = {}
    for k, v in trends_dict.items():
        trends_data[k] = v.raw

    # Step 2: Separate fields into different dictionaries based on their types
    data = {**assets_data, **trends_data}
    # separate the fields
    text_list = separate_fields(data)

    # Step 3: Generate embeddings for the text
    embeddings = generate_embedding(text_list)

    # Step 4: Upsert the data into the Pinecone index
    upsert_data('invest-data', text_list, embeddings)
    
