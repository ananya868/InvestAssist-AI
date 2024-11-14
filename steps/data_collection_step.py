from AI_Agents.assets_agent_call import AssetAnalysisAgent
from AI_Agents.trends_agent_call import MarketTrendsAgent
from steps.save_data import SaveData



def data_collection_step(asset_agent_list: list=['all'], trends_agent_list: list=['all'], llm_model: str='gpt-3.5-turbo'):
    """  
    This function runs the data collection step to generate real-time assets and trends data from the internet! 
    It runs crew ai agents taking certain prompts, you might tune these prompts according to your needs.
    """ 
    # Run agents 
    try:
        assets_dict = AssetAnalysisAgent(agent_list=asset_agent_list, llm_model=llm_model)
        print("[info] --Asset Agents ran successfully!--")
    except Exception as e:
        print(f"[error] --Asset Agents failed!-- {e}")
    
    try: 
        trends_dict = MarketTrendsAgent(agent_list=trends_agent_list, llm_model=llm_model)
        print("[info] --Trend Agents ran successfully!--")
    except Exception as e:
        print(f"[error] --Trend Agents failed!-- {e}")
    

    # Check and Save data 
    try:
        for asset_name, asset_data in assets_dict.items(): 
            saver = SaveData(destination='knowledge_base', data_field=asset_name)
            dt_01 = saver.check(asset_data.raw) # returns error if data is not valid
            asset_data_dict = saver.save() # saves data to json file
        print("[info] --Asset Data saved successfully!--")
    except Exception as e:
        print(f"[error] --Asset Data failed!-- {e}")
    
    try:
        for trend_name, trend_data in trends_dict.items():
            saver = SaveData(destination='knowledge_base', data_field=trend_name)
            dt_02 = saver.check(trend_data.raw)
            trend_data_dict = saver.save()
        print("[info] --Trend Data saved successfully!--")
    except Exception as e:
        print(f"[error] --Trend Data failed!-- {e}")
    
    # pass 
    return assets_dict, trends_dict




