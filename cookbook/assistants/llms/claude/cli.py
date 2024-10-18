import argparse
from phi.assistant import Assistant
from phi.tools.exa import ExaTools
from phi.tools.website import WebsiteTools
from phi.llm.anthropic import Claude

def main():
    parser = argparse.ArgumentParser(description='Chromatic Homotopy Theory Assistant')
    parser.add_argument('--query', type=str, help='Initial query to process')
    args = parser.parse_args()

    assistant = Assistant(llm=Claude(), tools=[ExaTools(), WebsiteTools()], show_tool_calls=True)

    if args.query:
        process_query(assistant, args.query)

    while True:
        user_input = input("Enter your query (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        process_query(assistant, user_input)

def process_query(assistant, query):
    assistant.print_response(
        query,
        markdown=True
    )

if __name__ == "__main__":
    main()