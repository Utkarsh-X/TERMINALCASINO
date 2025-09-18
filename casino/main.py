from casino.games.blackjack import play_blackjack
import pyfiglet
from colorama import Fore, Style, init
from InquirerPy import inquirer, get_style
import shutil

# Initialize colorama
init(autoreset=True)


def center_text(text: str) -> str:
    """Center text in the terminal width."""
    terminal_width = shutil.get_terminal_size().columns
    return "\n".join(line.center(terminal_width) for line in text.splitlines())


def show_welcome_screen():
    # Generate ASCII Art with pyfiglet
    text = "\nTERMINAL CASINO"
    font = "standard"
    ascii_art = pyfiglet.figlet_format(text, font=font)

    # Add color to ASCII art text
    colored_ascii_art = f"{Fore.WHITE}{ascii_art}{Style.RESET_ALL}"

    # Print centered ASCII art
    print(center_text(colored_ascii_art))

    # Define a custom style for InquirerPy
    style = get_style(
        {
            "questionmark": "#ff8559 bold",
            "answer": "#ff8559 bold",
            "pointer": "#ff8559 bold",
            "highlighted": "fg:#000000 bg:#00bfff bold",
            "selected": "fg:#ff8559 bold",
        }
    )

    terminal_width = shutil.get_terminal_size().columns

    pointer_padding1 = " " * (
        terminal_width // 2 - len("Please choose an option") // 2 - 2
    )
    pointer_padding2 = " " * (terminal_width // 2 - len("Play Blackjack") // 2 - 2)
    centered_pointer = pointer_padding2 + ">"

    # Ask user with styled menu (plain ASCII, centered)
    choice = inquirer.select(
        message=f"{pointer_padding1}Please choose an option",
        choices=[
            "Play Blackjack",
            "     Exit",
        ],
        style=style,
        transformer="",
        qmark="",
        pointer=centered_pointer,  # plain pointer
    ).execute()

    return choice


if __name__ == "__main__":
    choice = show_welcome_screen()

    if choice.startswith("Play"):
        play_blackjack()
    elif choice.startswith("Exit"):
        print(
            Fore.RED
            + "Goodbye! Thanks for visiting the Terminal Casino"
            + Style.RESET_ALL
        )
