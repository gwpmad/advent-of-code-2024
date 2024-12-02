from typing import Optional

from utils import open_file


def solution(values=open_file("2").split("\n")):
    return (solution_1(values), solution_2(values))


def solution_1(reports: list[str]) -> int:
    result = 0
    for report in reports:
        numbers = [*map(int, report.split())]
        failed_idx = find_failed_idx(numbers)
        if not isinstance(failed_idx, int):
            result += 1

    return result


def solution_2(reports: list[str]) -> int:
    result = 0
    for report in reports:
        numbers = [*map(int, report.split())]
        failed_idx = find_failed_idx(numbers)
        if isinstance(failed_idx, int) and all(
            isinstance(find_failed_idx(retry), int)
            for retry in [
                [n for i, n in enumerate(numbers) if i != failed_idx],
                [n for i, n in enumerate(numbers) if i != failed_idx + 1],
                [n for i, n in enumerate(numbers) if i != failed_idx - 1],
            ]
        ):
            continue
        result += 1
    return result


def find_failed_idx(numbers: list[int]) -> Optional[int]:
    increasing = numbers[1] > numbers[0]
    for i in range(0, len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]
        if ((difference > 0) != increasing) or difference == 0 or abs(difference) > 3:
            return i
    return None


test_config = {
    "input": """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split(
        "\n"
    ),
    "expected_solution_1": 2,
    "expected_solution_2": 4,
}
