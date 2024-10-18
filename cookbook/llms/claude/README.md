# Adding Stock Research to Crontab

To run the stock research automation script daily at 9 AM, follow these steps:

1. Make the cron script executable:
   ```
   chmod +x run_stock_research_cron.sh
   ```

2. Add the script to crontab using our custom tool:
   ```
   ./add_to_cron.sh "0 9 * * *" "/full/path/to/run_stock_research_cron.sh"
   ```

This will run the script every day at 9 AM. Adjust the cron schedule as needed.

Alternatively, you can manually edit the crontab:

1. Open the crontab editor:
   ```
   crontab -e
   ```

2. Add the following line:
   ```
   0 9 * * * /full/path/to/run_stock_research_cron.sh
   ```

3. Save and exit the editor.

Make sure to replace "/full/path/to/" with the actual path to your script.
# Anthropic Claude

[Models overview](https://docs.anthropic.com/claude/docs/models-overview)

> Note: Fork and clone this repository if needed

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Set your `ANTHROPIC_API_KEY`

```shell
export ANTHROPIC_API_KEY=xxx
```

### 3. Install libraries

```shell
pip install -U anthropic duckduckgo-search duckdb yfinance exa_py phidata
```

### 4. Run Assistant

- stream on

```shell
python cookbook/llms/claude/assistant.py
```

- stream off

```shell
python cookbook/llms/claude/assistant_stream_off.py
```

### 5. Run Assistant with Tools

- YFinance

```shell
python cookbook/llms/claude/finance.py
```

- Data Analyst

```shell
python cookbook/llms/claude/data_analyst.py
```

- Exa Search

```shell
python cookbook/llms/claude/exa_search.py
```

### 6. Run Assistant with Structured output

```shell
python cookbook/llms/claude/structured_output.py
```
