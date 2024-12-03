from pathlib import Path
import sys
import typing
from colorama import init, Fore
from enum import Enum


class Flags(Enum):
    PATH = "path"
    INDENT = "indent"


init(autoreset=True)


def is_valid_absolute_path(path: Path) -> bool:
    return Path(path).is_absolute() and Path(path).exists()


def parse_arguments(args: list[str]) -> typing.Dict[str, str]:
    arguments = {}

    for arg in args[1:]:
        if arg.startswith("--"):
            key, value = arg[2:].split("=", 1)
            arguments[key] = value

    return arguments


def print_directory_structure(path: Path, indent: str = " ", is_root: bool = False):
    path_obj = Path(path)

    if not path_obj.exists():
        raise Exception(f"{path} does not exist")

    if not path_obj.is_dir():
        raise Exception(f"{path} is not a directory")

    for item in path_obj.iterdir():
        if item.is_dir():
            print(Fore.BLUE + f"{indent}{'📦' if is_root else '📂'} {item.name}")
            print_directory_structure(item, indent + "  ")
        elif item.is_file():
            print(Fore.GREEN + f"{indent}📜 {item.name}")


def main():
    try:
        args = parse_arguments(sys.argv)
        path_arg = args.get(f"{Flags.PATH.value}")
        indent_arg = args.get(f"{Flags.INDENT.value}", " ")

        if not path_arg:
            raise Exception(
                "You should provide the absolute path to the file as the '--path=<your_abs_path>' argument in the CLI."
                f"\n{'-' * 120}"
                "\nUse the 'pwd' command to check your current absolute path."
            )
        path_obj = Path(path_arg)

        if not path_obj.is_absolute():
            path_obj = Path.cwd() / path_obj

        if not is_valid_absolute_path(path_obj):
            raise Exception(
                "your absolute path must be correct and exist on your pc"
                f"\n{'-' * 120}"
                "\nThis must be a directory"
            )
        else:
            return print_directory_structure(path_arg, is_root=True, indent=indent_arg)

    except Exception as e:
        print(Fore.RED + f"❌ Error: {e}")
        return None


if __name__ == "__main__":
    main()
