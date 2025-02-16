# QA agent

QA tool powered by LLM agents

## Quick start

Add API keys which you want to use to your .env file.

```
OPENAI_API_KEY=
GEMINI_API_KEY=
```

```bash
uv run src/main.py --uri examples/cases.csv --provider openai --model gpt-4o-mini --allowed-domains google.com --initial-url "https://www.google.com" --language ja
```
