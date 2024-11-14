from AI_Agents.real_time_assets_call import real_time_assets_agent
from AI_Agents.trends_agent_call import MarketTrendsAgent
from steps.save_data import SaveData



def real_time_data_collection_step(run: str='all', llm_model='gpt-3.5-turbo'):
    # Define the function to collect real-time data from the web
    
    try:
        assets_dict = real_time_assets_agent(run=run, llm_model=llm_model)
        print("[info] --Asset Agents ran successfully!--")
    except Exception as e:
        print(f"[error] --Asset Agents failed!-- {e}")
    
    try: 
        trends_dict = MarketTrendsAgent(agent_list=['all'], llm_model=llm_model)
        print("[info] --Trend Agents ran successfully!--")
    except Exception as e:
        print(f"[error] --Trend Agents failed!-- {e}")
    

    # Check and Save data
    save_path = 'knowledge_base/real_time_data'
    # make this path if not exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    try:
        for asset_name, asset_data in assets_dict.items():
            saver = SaveData(destination=save_path, data_field=asset_name)
            dt_01 = saver.check(asset_data)
            asset_data_dict = saver.save()
        print("[info] --Asset Data saved successfully!--")
    except Exception as e:
        print(f"[error] --Asset Data failed!-- {e}")
    
    try:
        for trend_name, trend_data in trends_dict.items():
            saver = SaveData(destination=save_path, data_field=trend_name)
            dt_02 = saver.check(trend_data)
            trend_data_dict = saver.save()
        print("[info] --Trend Data saved successfully!--")
    except Exception as e:
        print(f"[error] --Trend Data failed!-- {e}")

    # pass 
    return assets_dict, trends_dict