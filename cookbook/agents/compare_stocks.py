from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

def get_stock_tickers():
    ticker1 = input("Enter the first stock ticker: ").upper()
    ticker2 = input("Enter the second stock ticker: ").upper()
    return ticker1, ticker2

def compare_stocks(ticker1, ticker2):
    assistant = Assistant(
        llm=OpenAIChat(model="gpt-4"),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
        show_tool_calls=True,
    )
    comparison_prompt = f"Compare {ticker1} to {ticker2}. Use every tool you have"
    assistant.print_response(comparison_prompt, markdown=True)

if __name__ == "__main__":
    ticker1, ticker2 = get_stock_tickers()
    compare_stocks(ticker1, ticker2)
