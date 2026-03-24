#!/usr/bin/env python3
"""
Moonbeam — Kids' Sleep Time AI Assistant
Run with: python -m sleep_agent
"""

import os
import sys

from .agent import SleepAgent
from .commands import resolve_command
from .display import (
    clear_thinking,
    show_error,
    show_help,
    show_moonbeam,
    show_thinking,
    show_user_prompt,
    show_welcome,
)
from .prompts import WELCOME_MESSAGE


def check_api_key():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "\nError: ANTHROPIC_API_KEY is not set.\n"
            "Copy .env.example to .env and add your API key.\n"
            "Get a key at: https://console.anthropic.com\n"
        )
        sys.exit(1)


def main():
    check_api_key()
    agent = SleepAgent()
    show_welcome(WELCOME_MESSAGE)

    while True:
        try:
            user_input = show_user_prompt()
        except (KeyboardInterrupt, EOFError):
            show_moonbeam("Sweet dreams! Goodnight. ✨")
            sys.exit(0)

        if not user_input.strip():
            continue

        if user_input.strip().lower() in ("exit", "quit", "bye"):
            show_moonbeam("Sweet dreams! Sleep tight. ✨")
            sys.exit(0)

        api_message, is_local = resolve_command(user_input)

        if is_local:
            show_help(WELCOME_MESSAGE)
            continue

        show_thinking()
        try:
            response = agent.chat(api_message)
        except Exception as e:
            clear_thinking()
            show_error(str(e))
            continue

        clear_thinking()
        show_moonbeam(response)

        if user_input.strip().lower() == "/goodnight":
            sys.exit(0)


if __name__ == "__main__":
    main()
