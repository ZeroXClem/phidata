import os
import sys
import pathlib
from phidata.assistant import Assistant
from phidata.tools.yfinance import YFinanceTools
from phidata.llm.anthropic import Claude
import smtplib
from email.mime.text import MIMEText

# Find the path to the phidata project
try:
    # When running from a script
    current_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    # When running interactively
    current_dir = os.path.abspath(os.getcwd())
phidata_path = str(pathlib.Path(current_dir).parent)
sys.path.append(phidata_path)

# Define the list of 30 stocks to research
stock_tickers = ["AAPL", "MSFT", "AMZN", "GOOG", "TSLA", "FB", "NVDA", "JPM", "V", "JNJ", "WMT", "PG", "UNH", "MA", "HD", "DIS", "PYPL", "ADBE", "CSCO", "PFE", "INTC", "T", "VZ", "PEP", "MRK", "COST", "ABBV", "CMCSA", "LLY", "KO"]

# Set up the AI assistant with the YFinanceTools
assistant = Assistant(
    llm=Claude(model="claude-3-5-sonnet-20240620"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Use tables to display data where possible."],
    markdown=True,
)

# Loop through the list of stocks and gather the research
email_body = ""
for ticker in stock_tickers:
    email_body += f"## {ticker}

"
    response = assistant.print_response(f"Summarize fundamentals for {ticker}")
    email_body += response + "

"

# Send the email
sender = "your_email@example.com"
recipient = "user_email@example.com"
subject = "Stock Research Automation Results"
msg = MIMEText(email_body, "html")
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = recipient

with smtplib.SMTP("localhost") as smtp:
    smtp.send_message(msg)

print("Email sent successfully!")
