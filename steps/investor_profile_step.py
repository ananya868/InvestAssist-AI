from abc import ABC, abstractmethod
from profiler.investor_profile_data.input_data import *
from profiler.investor_profile_data.investor_insights import *
from profiler.investor_profile_data.json_build import build_json
from profiler.investor_profile_data.pdf_agent import build_pdf


# Define a class for Investor profile data input processing 
class InvestorProfile:
    def __init__(
        self, 
        investor_name: str,
        basic_info: dict, # 4 items
        financial_goals: dict, # 2 items
        historical_investment_behavior: dict,
        investment_horizon: dict,
        investment_preferences: dict,
        liquidity_needs: dict,
        other_info: dict, 
        risk_tolerance: dict,
        filename: str,
        save_pdf: bool,
    ):
        self.investor_name = investor_name
        self.basic_info = basic_info
        self.financial_goals = financial_goals
        self.historical_investment_behavior = historical_investment_behavior
        self.investment_horizon = investment_horizon
        self.investment_preferences = investment_preferences
        self.liquidity_needs = liquidity_needs
        self.other_info = other_info
        self.risk_tolerance = risk_tolerance
        self.filename = filename
        self.save_pdf = save_pdf
    
    def build(self):
        """ 
        This function will run the steps to generate the investor profile data
        Args:
            - All input data
        Returns:
            - json_data: dict
            - current_portfolio_insight: dict
            - financial_goals_insight: dict
            - risk_tolerance_insight: dict
        """
        # Current Portfolio 
        current_portfolio_extractor = CurrentPortfolioAssessmentAugmented(self.basic_info, self.historical_investment_behavior, self.api_key)
        current_portfolio_insight = current_portfolio_extractor.augment_data()

        # Financial Goals 
        financial_goals_extractor = FinancialGoalsAugmented(self.financial_goals, self.investment_preferences, self.api_key)
        financial_goals_insight = financial_goals_extractor.augment_data()

        # Risk Tolerance 
        risk_tolerance_extractor = RiskToleranceAugment(self.risk_tolerance, self.liquidity_needs, self.api_key)
        risk_tolerance_insight = risk_tolerance_extractor.augment_data()

        ## Build json for the profile 
        json_builder = build_json.BuildJson(
            self.basic_info, 
            self.financial_goals, 
            self.risk_tolerance, 
            self.historical_investment_behavior, 
            self.investment_horizon, 
            self.investment_preferences, 
            self.liquidity_needs, 
            self.other_info
        )
        json_data = json_builder.build_json()
        json_builder.save_json() # saves json data

        ## PDF Builder 
        # convert json to list
        data_list = [json_data['basic_info'], json_data['financial_goals'], json_data['risk_tolerance'], json_data['historical_investments'], json_data['investment_horizon'], json_data['investment_preferences'], json_data['liquidity_needs'], json_data['other_info']]
    
        pdf_builder = build_pdf.BuildPdf(pdf_filename=self.filename)
        pdf_name = f"{self.investor_name} - Investor Profile"
        if save_pdf: 
            pdf_builder.PDFtemplate(sentences=data_list, title_font='Times-Roman', pdf_title=pdf_name, unique_id=json_data['unique_id'], body_font='Helvetica', body_font_size=10)

        return json_data, current_portfolio_insight, financial_goals_insight, risk_tolerance_insight
    

