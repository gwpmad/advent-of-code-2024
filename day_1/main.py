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
    length_of_line = string.find("\n")
    state = {
        "R": defaultdict(int),
        "L": defaultdict(int),
        "total": 0,
    }
    for i in range(0, len(string), length_of_line + 1):
        substring = string[i : i + length_of_line + 1]
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

# keep dict of stacks and counts for each number for both left and right, and total starting 0

# { R: {}, L: {}, total: 0}
# 3   4
# { L: {3: 1}, R: {4: 1}, total: 0}
# 4   3
# do the addition both times after parsing number. [if it's more than 0 in other dict]
# { L: {3: 1, 4: 1}, R: {4: 1}, total: 0}
# total += ((4 * 1 * 1) - (4 * 0 * 1) = 4) = 4
# { L: {3: 1, 4: 1}, R: {3: 1, 4: 1}, total: 4}
# total += ((3 * 1 * 1) - (3 * 0 * 1) = 3) = 7
# { L: {3: 1, 4: 1}, R: {3: 1, 4: 1}, total: 7}
# 2   5
# { L: {2: 1, 3: 1}, R: {3: 1, 4: 1, 5: 1}, total: 7}
# 1   3
# { L: {1: 1, 2: 1, 3: 1}, R: {3: 1, 4: 1, 5: 1}, total: 7}
# { L: {1: 1, 2: 1, 3: 1}, R: {3: 2, 4: 1, 5: 1}, total: 7}
# total += ((3 * 1 * 2) - (3 * 1 * 1) = 3) = 10
# 3   9
# { L: {1: 1, 2: 1, 3: 2}, R: {3: 2, 4: 1, 5: 1}, total: 10}
# total += ((3 * 2 * 2) - (3 * 1 * 2) = 6) = 16
# { L: {1: 1, 2: 1, 3: 2}, R: {3: 2, 4: 1, 5: 1, 9: 1}, total: 16}
# 3   3
# { L: {1: 1, 2: 1, 3: 3}, R: {3: 2, 4: 1, 5: 1, 9: 1}, total: 16}
# total += ((3 * 3 * 2) - (3 * 2 * 2) = 6) = 22
# { L: {1: 1, 2: 1, 3: 3}, R: {3: 3, 4: 1, 5: 1, 9: 1}, total: 22}
# total += ((3 * 3 * 3) - (3 * 3 * 2) = 9) = 31
