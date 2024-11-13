from abc import ABC, abstractmethod
from profiler.investor_profile_data.json_build import build_json
from profiler.investor_profile_data.pdf_agent.build_pdf import BuildPDF
from profiler.investor_profile_data.investor_insights.current_portfolio_extractor import CurrentPortfolioAssessmentAugment
from profiler.investor_profile_data.investor_insights.financial_goals_extractor import FinancialGoalsAugment
from profiler.investor_profile_data.investor_insights.risk_tolerance_extractor import RiskToleranceAugment

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
        api_key: str
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
        self.api_key = api_key
    
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
        current_portfolio_extractor = CurrentPortfolioAssessmentAugment(self.basic_info, self.historical_investment_behavior, self.api_key)
        current_portfolio_insight = current_portfolio_extractor.augment_data()

        # Financial Goals 
        financial_goals_extractor = FinancialGoalsAugment(self.financial_goals, self.investment_preferences, self.api_key)
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

        # List of Inputs for pdf
        data_list = []
        for key, value in json_data.items():
            if key == 'basic_info':
                data_list.append(f"Name: {value['Name']}\nAge: {value['Age']}\nOccupation: {value['Occupation']}\nAnnual Income: {value['Annual Income']}\nNet Worth: {value['Net Worth']}")
            elif key == 'financial_goals':
                data_list.append(f"Financial Goals: \nPrimary Goal: {value['Primary Goal']} \nSecondary Goal: {value['Secondary Goal']}")
            elif key == 'risk_tolerance':
                data_list.append(f"Risk Tolerance: \n{value['Risk Tolerance']}")
            elif key == 'historical_investments':
                data_list.append(f"Historical Investment Behavior: \n{value['Historical investments']}")
            elif key == 'investment_horizon':
                data_list.append(f"Investment Horizon: \nShort term: {value['Short Term']} and \nLong term: {value['Long Term']}")
            elif key == 'investment_preferences':
                data_list.append(f"Investment Preferences: \n{value['Investment Preferences']}")
            elif key == 'liquidity_needs':
                data_list.append(f"Liquidity Needs: \n Emergency funds: {value['Emergency Funds']}")
            elif key == 'other_info':
                data_list.append(f"Other Info: \n{value}")

        # PDF Builder 
    
        pdf_builder = BuildPDF(pdf_filename=self.filename)
        pdf_name = f"{self.investor_name} - Investor Profile"
        
        try:
            if self.save_pdf: 
                pdf_builder.PDFtemplate(sentences=data_list, title_font='Times-Roman', pdf_title=pdf_name, unique_id=json_data['unique_id'], body_font='Helvetica', body_font_size=10)
            print("[info] --Pdf saved to dir successfully--")
        except Exception as e:
            print(f"[error] --Error saving pdf to dir-- {e}")

        return json_data, current_portfolio_insight, financial_goals_insight, risk_tolerance_insight

