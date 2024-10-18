"""
This script initializes an AI assistant using the phi library and OpenAI's GPT-4 model.
The assistant is equipped with DuckDuckGo search capabilities and is set to print its responses in markdown format.
"""

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

def initialize_assistant():
    """Initialize and return an AI assistant with web search capabilities."""
    return Assistant(llm=OpenAIChat(model="gpt-4o"), tools=[DuckDuckGo()], show_tool_calls=True)

def query_assistant(assistant, query):
    """Send a query to the assistant and print the response."""
    try:
        assistant.print_response(query, markdown=True)
    except Exception as e:
        print(f"An error occurred while querying the assistant: {str(e)}")

if __name__ == "__main__":
    try:
        assistant = initialize_assistant()
        query_assistant(assistant, "Share 3 news stories from France")
    except Exception as e:
        print(f"An error occurred during initialization: {str(e)}")