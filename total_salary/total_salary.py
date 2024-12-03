from pathlib import Path
import typing


def count_salaries(salaries: typing.List[str]) -> typing.List[float]:
    total_salaries = []

    for line in salaries:
        try:
            if not line.strip():
                continue

            _, salary = line.split(",")
            salary = float(salary.strip())
            if salary < 0:
                raise ValueError(f"Salary not able to be negative: {salary}")
            total_salaries.append(salary)
        except ValueError as e:
            print(e)
    return total_salaries


def total_salary(path: Path) -> typing.Tuple[float, float] | typing.Tuple[None, None]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.read().strip().split("\n")
            
            if not lines:
                return (None, None)

            salaries = count_salaries(lines)

            if not salaries:
                return (None, None)

            total_salary = sum(salaries)
            average_salary = total_salary / len(salaries)
            return (total_salary, average_salary)
    except FileNotFoundError:
        print(f"File not found: {path}")
    except IOError as e:
        print(f"Error reading file: {e}")
    return (None, None)


path = Path("salary_file.txt")
total, average = total_salary(path)

if total is None or average is None:
    print("Неможливо вирахувати загальну та середню зп")
else:
    print(
        f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}"
    )
