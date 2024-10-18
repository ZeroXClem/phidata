import asyncio
import datetime
import time
import datetime
import asyncio

import time
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

def get_user_topic():
    return input("Enter the topic for the report: ")

async def generate_report(topic):
    assistant = Assistant(llm=OpenAIChat(model="gpt-4"), tools=[DuckDuckGo()], show_tool_calls=True)
    start_time = time.time()
    full_report = ""
    async for chunk in assistant.astream(f"Provide a comprehensive report on {topic}"):
        print(chunk, end='', flush=True)
        full_report += chunk
        if time.time() - start_time >= 15 and not hasattr(generate_report, 'save_option_asked'):
            generate_report.save_option_asked = True
            save_option = input("\n\nDo you want to save the report when it's complete? (y/n): ")
            generate_report.save_choice = save_option.lower() == 'y'
    return full_report

def save_report(topic, report):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"{topic}_{current_date}.txt"
    with open(filename, 'w') as file:
        file.write(report)
    print(f"Report saved as {filename}")

async def main():
    topic = get_user_topic()
    report = await generate_report(topic)
    if hasattr(generate_report, 'save_choice') and generate_report.save_choice:
        save_report(topic, report)

if __name__ == "__main__":
    asyncio.run(main())