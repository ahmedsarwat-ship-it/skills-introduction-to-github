# Moonbeam — Kids' Sleep Time AI Assistant

Moonbeam is a gentle, kid-friendly AI assistant that helps children wind down and fall asleep at bedtime. It tells calming stories, guides breathing exercises, counts sheep, and more — all in a soothing, child-safe tone powered by Claude.

## Setup

### 1. Get an API Key

Sign up at [console.anthropic.com](https://console.anthropic.com) and create an API key.

### 2. Configure Your API Key

```bash
cp .env.example .env
# Open .env and set: ANTHROPIC_API_KEY=sk-ant-...
```

> **Important:** Never commit your `.env` file — it's already in `.gitignore`.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Moonbeam

```bash
python -m sleep_agent
```

## Available Commands

Once running, type any of these (or just chat freely):

| Command       | What it does                                      |
|---------------|---------------------------------------------------|
| `/story`      | Moonbeam tells a gentle, original bedtime story   |
| `/breathe`    | Guided 4-7-8 breathing exercise                   |
| `/sheep`      | Count cozy, fluffy sheep together                 |
| `/music`      | Describes peaceful sounds (rain, waves, forest…)  |
| `/tip`        | One helpful sleep tip for kids                    |
| `/goodnight`  | Warm farewell and the session ends                |
| `/help`       | Show this command list again                      |
| `exit` / `quit` / `bye` | Exit Moonbeam                         |

You can also just type anything — Moonbeam will respond in a calm, soothing way and gently steer the conversation toward sleep.

## How It Works

Moonbeam is built on the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python) using `claude-opus-4-6`. It maintains a full multi-turn conversation history so context is preserved throughout the session (e.g., if you tell Moonbeam your name, it will use it for the rest of the session).

Slash commands are translated into natural-language messages before being sent to the model, so the conversation history stays coherent.

## Project Structure

```
sleep_agent/
  __init__.py    — Package marker
  prompts.py     — Moonbeam system prompt and welcome message
  agent.py       — Anthropic SDK wrapper with conversation history
  commands.py    — Slash-command dispatch
  display.py     — Rich terminal rendering
  main.py        — CLI entry point
requirements.txt — Python dependencies
.env.example     — API key template
```
