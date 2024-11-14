from primary_agents.diversification_recommendation_agent import DiversifyAgent
from primary_agents.insights_gen_agent import InsightGeneratorAgent
from primary_agents.investment_recommendation import InvestmentRecommenderAgent



def recommendation_generation_step(
    asset_data: str, 
    trend_data: str,
    portfolio_data: str,
    financial_goals: str,
    risk_tolerance: str,
    api_key: str,
    agent_list: list=['all'], 
    model: str='gpt-3.5-turbo'
    ): 
    """ 
    This function utilize primary agents to generate recommendations and save it 
    Args:
        agent_list: list of agents to be used for recommendation generation
    Returns: None
    """ 
    # check if the list is empty using assert 
    assert agent_list, "Agent list cannot be empty"

    all_agents = ['Diversify', 'InsightsGen', 'InvestmentRecommender']
    if agent_list == ['all']:
        agents = all_agents
    else:
        agents = agent_list
    
    # Initialize the agents
    for agent in agents:
        if agent == 'Diversify':
            diversify_agent = DiversifyAgent(
                current_portfolio=portfolio_data,
                financial_goals=financial_goals,
                risk_tolerance=risk_tolerance,
                summarized_asset_data=asset_data,
                trends_data=trend_data,
                api_key=api_key,
                model=model
            )
            # Generate recommendation 
            response = diversify_agent.generate_recommendation()
            assert response, "Recommendation is empty!, Please check the agent or re-run."
            # Format the recommendation
            diversification_recommendation = diversify_agent.format(response)
            assert diversification_recommendation, "Recommendation is empty!, Failed to format"
            # Save the recommendation
            diversify_agent.save(diversification_recommendation)

        if agent == 'InsightsGen':
            insights_agent = InsightGeneratorAgent(
                current_portfolio=portfolio_data,
                summarized_asset_data=asset_data,
                trends_data=trend_data,
                api_key=api_key,
                model=model
            )
            # Generate insights
            response = insights_agent.generate_insights()
            assert response, "insights is empty!, Please check the agent or re-run."
            # Format the insights
            insights = insights_agent.format(response)
            assert insights, "insights is empty!, Failed to format"
            # Save the insights
            insights_agent.save(insights)

        if agent == 'InvestmentRecommender':
            investment_agent = InvestmentRecommenderAgent(
                current_portfolio=portfolio_data,
                financial_goals=financial_goals,
                summarized_asset_data=asset_data,
                trends_data=trend_data,
                api_key=api_key,
                model=model
            )
            # Generate recommendation
            response = investment_agent.generate_recommendation()
            assert response, "Recommendation is empty!, Please check the agent or re-run."
            # Format the recommendation
            investment_recommendation = investment_agent.format(response)
            assert investment_recommendation, "Recommendation is empty!, Failed to format"
            # Save the recommendation
            investment_agent.save(investment_recommendation)

    # return as a dict 
    return {
        'diversification_recommendation': diversification_recommendation,
        'insights': insights,
        'investment_recommendation': investment_recommendation
    }




