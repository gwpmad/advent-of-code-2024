from collections import defaultdict
from functools import reduce

from utils import open_file


def solution(values=open_file("1").split("\n")):
    return (solution_1(values), solution_2(values))


def solution_1(values: list[str]) -> int:
    left_list, right_list = get_int_lists(values)
    left_list.sort()
    right_list.sort()

    return reduce(
        lambda acc, idx_value: acc
        + (
            right_list[idx_value[0]] - idx_value[1]
            if right_list[idx_value[0]] > idx_value[1]
            else idx_value[1] - right_list[idx_value[0]]
        ),
        enumerate(left_list),
        0,
    )


def solution_2(values: list[str]) -> int:
    left_list = []
    right_list_occurrences = defaultdict(int)
    for value in values:
        numbers = value.split("   ")
        left_list.append(int(numbers[0]))
        right_list_occurrences[int(numbers[1])] += 1
    return reduce(
        lambda acc, number: acc + (number * right_list_occurrences[number]),
        left_list,
        0,
    )


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
3   3""".split(
        "\n"
    ),
    "expected_solution_1": 11,
    "expected_solution_2": 31,
}
