import sys
from types import ModuleType


def main() -> None:
    import importlib

    day_number = sys.argv[1]
    day = importlib.import_module(f"day_{day_number}.main")

    _assert_tests_passed(day)

    if not _is_test_only_mode() and _real_input_exists(day_number):
        solution = day.solution()
        print(f"Solution for day {day_number}:\n1: {solution[0]}\n2: {solution[1]}")


def _assert_tests_passed(day: ModuleType) -> None:
    test_solution = day.solution(values=day.test_config["input"])
    expected_solution_1 = day.test_config["expected_solution_1"]
    expected_solution_2 = day.test_config["expected_solution_2"]
    assert (
        test_solution[0] == expected_solution_1
    ), f"Expected {expected_solution_1} but got {test_solution[0]}"
    assert (
        test_solution[1] == expected_solution_2
    ), f"Expected {expected_solution_2} but got {test_solution[1]}"


def _is_test_only_mode() -> bool:
    return len(sys.argv) > 2 and sys.argv[2] == "testonly"


def _real_input_exists(day_number: str) -> bool:
    import os

    return os.stat(f"day_{day_number}/input").st_size > 0


if __name__ == "__main__":
    main()
