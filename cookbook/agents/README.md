# Universal CLI for Web Search

This project provides a universal Command Line Interface (CLI) for web searches using the Phi framework and DuckDuckGo search engine.

## Setup

1. Install the required packages:
   ```
   pip install phi-framework
   ```

2. Set up your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

Run the CLI using:

```
python universal_cli.py
```

Enter your queries when prompted. The program will display the response and automatically save it to a Markdown file.

To exit the program, type 'quit' when prompted for a query.

## Features

- Uses GPT-4 for processing queries
- Integrates DuckDuckGo for web searches
- Automatically saves responses to Markdown files
- Continuous query loop until user chooses to quit
# Advanced Research Assistant

This project includes an advanced research assistant with CLI commands, steerability, and long-term query support.

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install phi-assistant openai yfinance duckduckgo-search argparse
   ```

## Usage

Run the advanced research assistant from the command line:

```
python advanced_research_assistant.py "Your research query here" --steer "Optional steering direction"
```

Example:
```
python advanced_research_assistant.py "Latest developments in AI" --steer "Focus on applications in healthcare"
```

The assistant will use its tools (YFinance and DuckDuckGo) to research the query and provide a comprehensive response. The conversation history is maintained for context in follow-up queries.
# Building Agents with gpt-4o

This cookbook shows how to build agents with gpt-4o

> Note: Fork and clone this repository if needed

### 1. Create a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Install libraries

```shell
pip install -r cookbook/agents/requirements.txt
```

### 3. Export credentials

- We use gpt-4o as the llm, so export your OpenAI API Key

```shell
export OPENAI_API_KEY=***
```

- To use Exa for research, export your EXA_API_KEY (get it from [here](https://dashboard.exa.ai/api-keys))

```shell
export EXA_API_KEY=xxx
```

### 4. Run PgVector

We use PgVector to provide long-term memory and knowledge to the LLM OS.
Please install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run PgVector using either the helper script or the `docker run` command.

- Run using a helper script

```shell
./cookbook/run_pgvector.sh
```

- OR run using the docker run command

```shell
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16
```

### 5. Run the App

```shell
streamlit run cookbook/agents/app.py
```

- Open [localhost:8501](http://localhost:8501) to view your LLM OS.

### 6. Message on [discord](https://discord.gg/4MtYHHrgA8) if you have any questions

### 7. Star ⭐️ the project if you like it.

### Share with your friends: https://phidata.link/agents
