from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    show_tool_calls=True,
)

def main():
    while True:
        user_input = input("What would you like to research? (Type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        assistant.print_response(f"Research the following topic: {user_input}. Use every tool you have.", markdown=True)
        print("\n---\n")

if __name__ == "__main__":
    main()