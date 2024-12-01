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
    state = {
        "R": defaultdict(int),
        "L": defaultdict(int),
        "total": 0,
    }
    for i in range(0, len(string), step_size):
        substring = string[i : i + step_size]
        left_digit, right_digit = list(map(int, substring.split()))

        state["L"][left_digit] += 1
        if state["R"][left_digit]:
            state["total"] += get_addition_to_subtotal(
                left_digit, state["L"][left_digit], state["R"][left_digit]
            )
        state["R"][right_digit] += 1
        if state["L"][right_digit]:
            state["total"] += get_addition_to_subtotal(
                right_digit, state["R"][right_digit], state["L"][right_digit]
            )
    return state["total"]


def get_addition_to_subtotal(
    digit: int, current_col_digit_count: int, opposite_col_digit_count: int
) -> int:
    return (current_col_digit_count * opposite_col_digit_count * digit) - (
        (current_col_digit_count - 1) * opposite_col_digit_count * digit
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
3   3""",
    "expected_solution_1": 11,
    "expected_solution_2": 31,
}
