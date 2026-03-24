COMMAND_PROMPTS = {
    "/story":      "Please start a gentle bedtime story for me.",
    "/breathe":    "Please guide me through a calming breathing exercise.",
    "/sheep":      "Please help me count sleepy sheep.",
    "/music":      "Please describe some peaceful, dreamy sounds to help me sleep.",
    "/tip":        "Please give me one helpful sleep tip.",
    "/goodnight":  "Please say goodnight to me.",
    "/help":       None,  # handled locally, no API call needed
}


def resolve_command(user_input: str):
    """
    Returns (api_message, is_local_command).
    api_message is None for local commands handled in the display layer.
    """
    stripped = user_input.strip().lower()
    if stripped not in COMMAND_PROMPTS:
        return user_input, False       # plain conversation
    if stripped == "/help":
        return None, True              # handled by display layer
    return COMMAND_PROMPTS[stripped], False
