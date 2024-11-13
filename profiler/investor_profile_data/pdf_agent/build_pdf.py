# Script for conversion of raw string inputs and build pdf
import os 
import PyPDF2 
import json
import pandas as pd

import reportlab 
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas 

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_JUSTIFY

from datetime import datetime



class BuildPDF:
    """
    Takes in json data and builds a pdf file
    """
    def __init__(self, pdf_filename: str):
        self.pdf_filename = pdf_filename 


    """PDF Creation"""
    def PDFtemplate(self, sentences: list, title_font: str, pdf_title: str, unique_id: str, 
                    body_font: str, title_font_size: int = 24, body_font_size: int = 12): 
        """     
        Create a PDF template
        """

        # Register some cool fonts 
        pdfmetrics.registerFont(TTFont('Forensic', 'profiler/investor_profile_data/pdf_agent/fonts/forensic.ttf'))
        pdfmetrics.registerFont(TTFont('JbMono', 'profiler/investor_profile_data/pdf_agent/fonts/JetBrainsMonoBold.ttf')) # Working 
        pdfmetrics.registerFont(TTFont('GeistMono', 'profiler/investor_profile_data/pdf_agent/fonts/GeistMonoVF.ttf'))

        # Set up the document 
        doc = SimpleDocTemplate(
            self.pdf_filename,
            pagesize=letter, # change it to A4 if need
            rightMargin=40, # right margin 
            leftMargin=40, # left margin
            topMargin=72, # top margin
            bottomMargin=18, # bottom margin
        )

        # get default styles and define custom styles if needed
        styles = getSampleStyleSheet()

        #  Title
        title_style = ParagraphStyle(
            # tweak these if needed
            name='Title',
            fontName=title_font,
            fontSize=title_font_size, 
            leading=30,
            spaceBefore=10,
            spaceAfter=20,
        )

        # Body 
        body_style = ParagraphStyle(
            name="BodyText",
            parent=styles["BodyText"],
            fontName=body_font, # font for body paragraph
            fontSize=body_font_size, # font size for body
            leading=10,
            spaceAfter=10,
            leftIndent=5,
            rightIndent=5,
            allowOrphans=1,
            allowWidows=1,
            alignment=TA_JUSTIFY
        )
        
        ## draw line in the canvas
        def draw_line(canvas, doc):
            canvas.saveState()
            width, height = letter
            canvas.setLineWidth(0.5)
            canvas.line(30, height - 120, width - 30, height - 120)

            # Get current date
            current_date = datetime.now().strftime("%Y-%m-%d")
            date_text = f"Date of creation: {current_date}"
            
            # Draw date at the top right corner
            canvas.setFont("Times-Roman", 10)
            text_width = canvas.stringWidth(f'<b>{date_text}</b>', "Times-Roman", 10)
            canvas.drawString(width - text_width - 40, height - 20, date_text)

            # Draw unique ID at the top left corner
            unique_id_text = f"ID# {unique_id}"
            canvas.drawString(40, height - 20, unique_id_text)

            canvas.restoreState()

        """List of Elements"""
        elements = []

        ## Add title to the PDF 
        title = pdf_title

        ## Tweak if needed
        # add title to list
        elements.append(Paragraph(title, title_style))
        # add space after title
        elements.append(Spacer(1, 20))

        
        def format_bold(text: str): 
            """
            Function to format text with bold tags
            """
            # List of words to be bolded
            bold_words = ['Name:', 'Age:', 'Occupation:', 'Annual Income', 'Net Worth:', 'Financial Goals:', 'Investment Horizon:', 'Risk Tolerance:',
                        'Investment Preferences:', 'Historical Investment Behavior:', 'Liquidity Needs:', 'Tax Consideration:'] # add all the words to be bolded
            for i in bold_words:
                text = text.replace(i, f"<b>{i}</b>")
            
            return text
        

        # Add each Sentence to the PDF 
        for sentence in sentences:
            # split it by n-line
            j = sentence.split('\n') # j -> list
            # append this list to elements list
            for i in j: 
                # i -> string 
                # format to bold
                i = format_bold(i)

                # append to para
                elements.append(Paragraph(i, body_style))
            elements.append(Spacer(1, 12)) # Give space


        # Build the PDF 
        doc.build(elements, onFirstPage=draw_line) # Saves the pdf automatically

        # Returns nothing 





# # example usage 
# ex = [
#     "Name: Arnav Kumar\nAge: 25\nOccupation: Data Scientist\nAnnual Income: $120000\nNet Worth: $100,000",
#     "Financial Goals: \nPrimary Goal: Retirement Savings \nSecondary Goal: Children Education loan",
#     "Investment Horizon: \nShort term: 1-3 years and \nLong term: 4-5 years",
#     "Risk Tolerance: \nHigh Risk Tolerance with careful investment in stocks. Comfortable with moderate market fluctuations.",
#     "Investment Preferences: \nStocks: 60% Bonds: 20% Mutual Funds: 10% Real Estate: 10%, Ethical Consideration: No drug company",
#     "Historical Investment Behavior: \nDiversified Portfolio with focus on real estate. Mutual fund and ETFs with low risk is also preferable",
#     "Liquidity Needs: \n Emergency funds: $50000 in a high yield savings account", 
#     "Tax Consideration: \n Utilize tax-advantage accounts such as 401k and ROTH IRA"
# ]

# pdf_ = BuildPDF(ex, 'profiler/pdf_profiles/example.pdf')
# pdf_.PDFtemplate(sentences=ex, title_font='Times-Roman', pdf_title=f'Arnav Kumar - Investor Profile', unique_id='9u124j002a', body_font='Helvetica', body_font_size=10)
    

        
        




    



