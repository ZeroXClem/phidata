from phi.assistant import Assistant
from phi.tools.yfinance import YFinanceTools
from phi.llm.groq import Groq
import schedule
import time
from notifiers import get_notifier

def analyze_stock(ticker):
    assistant = Assistant(
        llm=Groq(model="llama3-70b-8192"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
        show_tool_calls=True,
    )
    
    price = assistant.run(f"What's the {ticker} stock price")
    recommendations = assistant.run(f"Share {ticker} analyst recommendations")
    fundamentals = assistant.run(f"Summarize fundamentals for {ticker}")
    
    return f"Stock Analysis for {ticker}:\n\nPrice: {price}\n\nRecommendations: {recommendations}\n\nFundamentals: {fundamentals}"

def send_notification(message):
    telegram = get_notifier('telegram')
    telegram.notify(message=message, token='YOUR_BOT_TOKEN', chat_id='YOUR_CHAT_ID')

def job():
    tickers = ['NVDA', 'TSLA', 'AAPL']  # Add more tickers as needed
    for ticker in tickers:
        analysis = analyze_stock(ticker)
        send_notification(analysis)

schedule.every().day.at("09:00").do(job)  # Run daily at 9:00 AM

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)