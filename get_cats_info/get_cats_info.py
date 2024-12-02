from pathlib import Path
import typing


def get_cats_info(path: Path) -> typing.Dict[str, str | int] | None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.read().strip().split("\n")
            result_list = []

            if not lines:
                return None

            for line in lines:
                id, name, age = line.strip().split(",")
                cat = {"id": id, "name": name, "age": age}
                result_list.append(cat)

        return result_list
    except FileNotFoundError:
        print(f"File not found: {path}")
    except IOError as e:
        print(f"Error reading file: {e}")
    return None


path = Path("cats.txt")
print(get_cats_info(path))
