# from data_pipelines.asset_database_pipeline import AssetETL
# from asset_analysis_agent.build_agent import BuildAgent
# #### Pseudo code
# class RunDataPipeline: 
#     def __init__(self): 
#         pass 


#     def run_asset_data_pipeline():

#         stocks = ['stock', 'mutual_fund']
#         for i in stocks: 

#             # Agent 
#             agent = BuildAgent.build(i) # agent built 
#             data = agent.run() # data
            
#             # Data pipeline 
#             asset = AssetETL(output_dir='stocks', asset_type=i)
#             asset.extract(data) # Extract
#             asset.transform(Strategy) # Transform with some strategies of ur choice 
#             asset.load() 




        # once this runs, it ll use the agent to create data, then make changes/clean then save it on the database. 


    
# usage
from data_pipelines.trend_database_pipeline import TrendETL


data =  """Disclaimer: The following analysis is based on the information available as of October 23, 2024. Market conditions can change rapidly, and this analysis is not financial advice. Please consult with a financial advisor before making any investment decisions.

Last Week's Stock Market Overview

The past week witnessed a volatile trading environment, with major indices experiencing both gains and losses. Global economic uncertainties, geopolitical tensions, and corporate earnings reports all contributed to the market's fluctuations.

Key Developments:

Interest Rate Concerns: Investors remained cautious amid concerns about potential interest rate hikes by central banks to combat inflation. This uncertainty weighed on market sentiment.
Earnings Season: The release of corporate earnings reports led to mixed reactions from investors, with some companies exceeding expectations while others fell short.
Geopolitical Tensions: Ongoing geopolitical events, such as the Russia-Ukraine conflict and trade disputes, continued to create market volatility.
Sector Performance:

Technology: Technology stocks experienced a mixed performance, with some companies benefiting from strong earnings reports while others faced challenges in a competitive environment.
Healthcare: The healthcare sector remained relatively stable, supported by positive developments in drug approvals and medical advancements.
Energy: Energy stocks saw a surge due to rising oil prices and increased demand.
Financials: The financial sector was impacted by interest rate concerns and economic uncertainties.
Notable Stocks:

Company A: Shares of Company A surged after announcing strong quarterly earnings and a positive outlook.
Company B: Concerns about supply chain disruptions and rising costs weighed on Company B's stock price.
Company C: A new product launch boosted investor confidence in Company C, leading to a significant increase in its share price.
Overall Outlook:

The market remains uncertain, with investors closely monitoring economic indicators, corporate earnings, and geopolitical developments. While there are opportunities for growth, it's essential to approach investments with caution and consider your risk tolerance."""



asset = TrendETL(destination='knowledge_base', trend_type='market')
asset.extract(trend_data=data)
asset.transform(api_key='api_key')
asset.load()