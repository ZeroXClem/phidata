import argparse
from phi.assistant import Assistant
from phi.tools.yfinance import YFinanceTools
from phi.llm.groq import Groq

def perform_stock_research(ticker):
    assistant = Assistant(
        llm=Groq(model="llama3-70b-8192"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
        show_tool_calls=True,
    )

    print(f"\nResearching {ticker}...\n")

    # Get stock price
    price_response = assistant.run(f"What's the {ticker} stock price")
    print("Current Stock Price:")
    print(price_response)

    # Get analyst recommendations
    recommendations = assistant.run(f"Share {ticker} analyst recommendations")
    print("\nAnalyst Recommendations:")
    print(recommendations)

    # Get stock fundamentals
    fundamentals = assistant.run(f"Summarize fundamentals for {ticker}")
    print("\nStock Fundamentals:")
    print(fundamentals)

    # Get recent news
    news = assistant.run(f"Summarize recent news for {ticker}")
    print("\nRecent News:")
    print(news)

    # Generate insights for stock option traders
    insights = assistant.run(f"Based on the above information, provide insights and potential strategies for {ticker} stock option traders")
    print("\nInsights for Stock Option Traders:")
    print(insights)

def main():
    parser = argparse.ArgumentParser(description="Perform comprehensive stock research")
    parser.add_argument("ticker", type=str, help="Stock ticker symbol")
    args = parser.parse_args()

    perform_stock_research(args.ticker)

if __name__ == "__main__":
    main()