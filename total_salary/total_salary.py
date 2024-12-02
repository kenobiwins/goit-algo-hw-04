from pathlib import Path
import typing


def count_salaries(salaries: typing.List[str]) -> typing.List[int]:
    total_salaries = []

    for line in salaries:
        try:
            _, salary = line.split(",")
            salary = int(salary.strip())
            if salary < 0:
                raise ValueError(f"Salary not able to be negative: {salary}")
            total_salaries.append(salary)
        except ValueError as e:
            print(e)
    return total_salaries


def total_salary(path: Path) -> typing.Tuple[int, int] | None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.read().strip().split("\n")

            if not lines:
                return None

            salaries = count_salaries(lines)
            total_salary = sum(salaries)
            average_salary = total_salary // len(salaries)
            return (total_salary, average_salary)
    except FileNotFoundError:
        print(f"File not found: {path}")
    except IOError as e:
        print(f"Error reading file: {e}")
    return None


path = Path("salary_file.txt")
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
