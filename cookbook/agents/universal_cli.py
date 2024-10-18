import sys
from typing import Optional

from phi.tools.duckduckgo import DuckDuckGo
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

def save_to_markdown(query: str, response: str) -> None:
    filename = f"{query[:30].replace(' ', '_')}.md"
    try:
        with open(filename, 'w') as f:
            f.write(f"# Query: {query}\n\n{response}")
        print(f"Response saved to {filename}")
    except IOError as e:
        print(f"Error saving response to file: {e}")

def get_assistant() -> Assistant:
    return Assistant(llm=OpenAIChat(model="gpt-4"), tools=[DuckDuckGo()], show_tool_calls=True)

def process_query(assistant: Assistant, query: str) -> Optional[str]:
    try:
        response = assistant.run(query)
        print("Response:")
        print(response)
        save_to_markdown(query, response)
        return response
    except Exception as e:
        print(f"An error occurred while processing the query: {str(e)}")
        return None

def main() -> None:
    assistant = get_assistant()
    
    while True:
        query = input("Enter your query (or 'quit' to exit): ").strip()
        if query.lower() == 'quit':
            break
        
        process_query(assistant, query)
        print("\n---\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)