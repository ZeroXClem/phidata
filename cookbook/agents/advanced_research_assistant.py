import argparse
import sqlite3
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

class SQLiteMemory:
    def __init__(self, db_name='conversation_memory.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             role TEXT,
             content TEXT,
             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
        ''')
        self.conn.commit()

    def add(self, role, content):
        self.cursor.execute('INSERT INTO conversations (role, content) VALUES (?, ?)', (role, content))
        self.conn.commit()

    def get(self, limit=10):
        self.cursor.execute('SELECT role, content FROM conversations ORDER BY timestamp DESC LIMIT ?', (limit,))
        return [{'role': role, 'content': content} for role, content in self.cursor.fetchall()[::-1]]

class AdvancedResearchAssistant:
    def __init__(self):
        self.memory = SQLiteMemory()
        self.assistant = Assistant(
            llm=OpenAIChat(model="gpt-4"),
            tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
                   DuckDuckGo()],
            show_tool_calls=True
        )

    def research(self, query, steer=None):
        if steer:
            query = f"{query} Focus on: {steer}"
        response = self.assistant.chat(query)
        self.memory.add('human', query)
        self.memory.add('assistant', response)
        return query, response

    def run_cli(self):
        parser = argparse.ArgumentParser(description="Advanced Research Assistant")
        parser.add_argument("query", help="Research query")
        parser.add_argument("--steer", help="Steer the research in a specific direction")
        args = parser.parse_args()

        query, response = self.research(args.query, args.steer)
        print(f"Query: {query}\n\nResponse: {response}")

def main():
    assistant = AdvancedResearchAssistant()
    assistant.run_cli()

if __name__ == "__main__":
    main()