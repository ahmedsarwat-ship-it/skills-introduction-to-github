import os
from anthropic import Anthropic
from dotenv import load_dotenv
from .prompts import SYSTEM_PROMPT

load_dotenv()


class SleepAgent:
    def __init__(self):
        self.client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        self.conversation_history = []
        self.model = "claude-opus-4-6"

    def chat(self, user_message: str) -> str:
        self.conversation_history.append({
            "role": "user",
            "content": user_message,
        })

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=self.conversation_history,
        )

        assistant_message = response.content[0].text

        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message,
        })

        return assistant_message

    def reset_conversation(self):
        self.conversation_history = []
