from steps.summarizer import Summarizer



def summarizer_step(assets_dict: dict, trends_dict: dict, api_key: str): 
    """ 
    This function runs the summarization to generate concise summaries of asset and trends data
    It runs a large language model (LLM) using the OpenAI API to summarize the data into concise summaries for better analysis
    Args:
        - assets_dict: A dictionary containing asset data
        - trends_dict: A dictionary containing trend data
        - api_key: A string containing the OpenAI API key
    Returns:
        - summarized_asset_text: A string containing the summarized asset data
        - summarized_trends_text: A string containing the summarized trend data
    """ 
    try:
        asset_list = []
        for assets, assets_data in assets_dict.items():
            asset_list.append(assets_data)
        
        asset_summarizer = Summarizer(text_list=asset_list, sent_limit=200, api_key=api_key)
        summarized_asset_text = asset_summarizer.summarize()
        print("[info] --Asset Summarized successfully!--")
    except Exception as e:
        print(f"[error] --Asset Summarization failed!-- {e}")
    
    try:
        trend_list = []
        for trends, trends_data in trends_dict.items():
            trend_list.append(trends_data)
        
        trend_summarizer = Summarizer(text_list=trend_list, sent_limit=200, api_key=api_key)
        summarized_trends_text = trend_summarizer.summarize()
        print("[info] --Trend Summarized successfully!--")
    except Exception as e:
        print(f"[error] --Trend Summarization failed!-- {e}")
    
    return summarized_asset_text, summarized_trends_text




