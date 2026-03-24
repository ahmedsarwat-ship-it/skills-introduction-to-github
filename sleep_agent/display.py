from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

MOONBEAM_COLOR = "cyan"
BORDER_COLOR = "blue"


def show_welcome(message: str):
    panel = Panel(
        message,
        title="[cyan]✨ Moonbeam ✨[/cyan]",
        border_style=BORDER_COLOR,
        padding=(1, 2),
    )
    console.print(panel)


def show_moonbeam(message: str):
    text = Text(message, style=MOONBEAM_COLOR)
    console.print(
        Panel(
            text,
            title="[cyan]Moonbeam[/cyan]",
            border_style=BORDER_COLOR,
            padding=(0, 1),
        )
    )


def show_user_prompt() -> str:
    return console.input("\n[bright_white bold]You:[/bright_white bold] ")


def show_error(message: str):
    console.print(f"[red]Oops! {message}[/red]")


def show_help(welcome_message: str):
    console.print(
        Panel(
            welcome_message,
            title="[cyan]Help[/cyan]",
            border_style=BORDER_COLOR,
            padding=(1, 2),
        )
    )


def show_thinking():
    console.print("\n[dim]Moonbeam is thinking...[/dim]", end="")


def clear_thinking():
    console.print("\r" + " " * 30 + "\r", end="")
