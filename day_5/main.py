from collections import defaultdict
from collections.abc import Callable
from functools import cmp_to_key, reduce

from utils import open_file


def solution(values=open_file("5").split("\n\n")):
    updates = list(
        map(lambda update: list(map(int, update.split(","))), values[1].split("\n"))
    )
    lookup = reduce(_create_precedence_lookup, values[0].split("\n"), defaultdict(set))

    solution_1 = 0
    solution_2 = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(_get_comparator(lookup)))
        if sorted_update == update:
            solution_1 += _middle_entry(update)
        else:
            solution_2 += _middle_entry(sorted_update)

    return (solution_1, solution_2)


def _create_precedence_lookup(
    lookup: defaultdict[int, set], entry: str
) -> defaultdict[int, set]:
    former, latter = list(map(int, entry.split("|")))
    lookup[former].add(latter)
    return lookup


def _get_comparator(lookup: defaultdict[int, set]) -> Callable[[int, int], int]:
    def compare_by_precedence(a: int, b: int):
        if b in lookup[a]:
            return -1
        return 1 if a in lookup[b] else 0

    return compare_by_precedence


def _middle_entry(update: list[int]) -> int:
    return update[int(len(update) / 2)]


test_config = {
    "input": """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split(
        "\n\n"
    ),
    "expected_solution_1": 143,
    "expected_solution_2": 123,
}
