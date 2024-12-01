import time
from collections import defaultdict
from functools import reduce

from utils import open_file


def solution(values=open_file("1")):
    return (solution_1(values), solution_2(values))


def solution_1(values: str) -> int:
    left_list, right_list = get_int_lists(values.split("\n"))
    left_list.sort()
    right_list.sort()

    return reduce(
        lambda acc, idx_value: acc + (abs(right_list[idx_value[0]] - idx_value[1])),
        enumerate(left_list),
        0,
    )


def solution_2(string: str) -> int:
    step_size = string.find("\n") + 1
    left_counts, right_counts, total = defaultdict(int), defaultdict(int), 0
    for i in range(0, len(string), step_size):
        substring = string[i : i + step_size]
        left_digit, right_digit = list(map(int, substring.split()))

        left_counts[left_digit] += 1
        total += left_digit * right_counts[left_digit]

        right_counts[right_digit] += 1
        total += right_digit * left_counts[right_digit]
    return total


def get_int_lists(values: list[str]) -> tuple[list[int], list[int]]:
    left_list, right_list = [], []
    for value in values:
        ints = list(map(int, value.split("   ")))
        left_list.append(ints[0])
        right_list.append(ints[1])
    return left_list, right_list


test_config = {
    "input": """3   4
4   3
2   5
1   3
3   9
3   3""",
    "expected_solution_1": 11,
    "expected_solution_2": 31,
}
