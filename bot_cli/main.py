from colorama import Fore, init
from enum import Enum
from typing import Dict, Tuple

init(autoreset=True)


class Command(Enum):
    ADD = "add"
    CHANGE = "change"
    PHONE = "phone"
    ALL = "all"
    HELLO = "hello"
    EXIT = "exit"
    CLOSE = "close"
    HELP = "help"


class Color(Enum):
    SUCCESS = Fore.GREEN
    ERROR = Fore.RED
    INFO = Fore.BLUE
    WARNING = Fore.YELLOW
    TITLE = Fore.MAGENTA
    HIGHLIGHT = Fore.CYAN
    DEFAULT = Fore.WHITE


COMMAND_DESCRIPTIONS: Dict[Command, str] = {
    Command.ADD: "Add a new contact. Usage: add <name> <phone>",
    Command.CHANGE: "Change an existing contact's phone number. Usage: change <name> <phone>",
    Command.PHONE: "Show the phone number of a contact. Usage: phone <name>",
    Command.ALL: "Show all contacts.",
    Command.HELLO: "Greet the assistant.",
    Command.EXIT: "Exit the assistant.",
    Command.CLOSE: "Exit the assistant.",
    Command.HELP: "Show all available commands.",
}


def add_contact(args: list[str], contacts: Dict[str, str]) -> str:
    if len(args) < 2:
        return f"{Color.ERROR.value}Error: Please provide both name and phone number."
    else:
        name, phone = args
        contacts[name] = phone
        return f"{Color.SUCCESS.value}Contact added."


def change_contact(args: list[str], contacts: Dict[str, str]) -> str:
    if len(args) < 2:
        return f"{Color.ERROR.value}Error: Please provide both name and phone number."
    else:
        name, phone = args
        contacts[name] = phone
        return f"{Color.SUCCESS.value}Contact changed."


def show_phone(args: list[str], contacts: Dict[str, str]) -> str:
    if len(args) < 1:
        return f"{Color.ERROR.value}Error: Please provide a name."

    name, = args
    phone = contacts.get(name)
    if phone:
        return f"{Color.INFO.value}{name}: {phone}"
    return f"{Color.ERROR.value}Contact not found."


def parse_input(user_input: str) -> Tuple[str, list[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def show_all(contacts: Dict[str, str]) -> str:
    if not contacts:
        return f"{Color.WARNING.value}No contacts available."

    result = [f"{Color.HIGHLIGHT.value}All Contacts:"]
    for name, phone in contacts.items():
        result.append(f"{Color.INFO.value}{name}: {phone}")
    return "\n".join(result)


def show_help() -> str:
    result = [f"{Color.HIGHLIGHT.value}Available Commands:"]
    for command, description in COMMAND_DESCRIPTIONS.items():
        result.append(f"{Color.DEFAULT.value}{command.value}: {description}")
    return "\n".join(result)


def main() -> None:
    print(f"{Color.TITLE.value}Welcome to the assistant bot!")
    contacts = {}

    try:
        while True:
            user_input = (
                input(f"{Color.DEFAULT.value}Enter a command: ").strip().lower()
            )
            command, *args = parse_input(user_input)

            try:
                parsed_command = Command(command)
            except ValueError:
                print(
                    f"{Color.ERROR.value}Error: Invalid command. Type 'help' to see available commands for the CLI."
                )
                continue

            match parsed_command:
                case Command.EXIT | Command.CLOSE:
                    print(f"{Color.TITLE.value}Good bye!")
                    break
                case Command.HELLO:
                    print(f"{Color.TITLE.value}How can I help you?")
                case Command.ADD:
                    print(add_contact(args, contacts))
                case Command.CHANGE:
                    print(change_contact(args, contacts))
                case Command.PHONE:
                    print(show_phone(args, contacts))
                case Command.ALL:
                    print(show_all(contacts))
                case Command.HELP:
                    print(show_help())
                case _:
                    print(f"{Color.ERROR.value}Error: Invalid command.")
    except Exception as e:
        print(f"{Color.ERROR.value}Exeption: {e}")


if __name__ == "__main__":
    main()
