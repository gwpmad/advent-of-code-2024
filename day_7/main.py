from typing import Callable

from utils import open_file


def solution(values=open_file("7").split("\n")):
    queue = _get_initial_queue(values)
    return (solution_1(queue.copy()), solution_2(queue.copy()))


def solution_1(
    queue: list[dict],
):
    ops = [lambda x, y: x + y, lambda x, y: x * y]
    return _get_possible_eqations(queue, ops)


def solution_2(
    queue: list[dict],
):
    ops = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(f"{x}{y}")]
    return _get_possible_eqations(queue, ops)


def _get_initial_queue(values: list[str]) -> list[dict]:
    return [
        {
            "equation_idx": idx_line[0],
            "target": idx_line[1][0],
            "current": idx_line[1][1],
            "remaining": idx_line[1][2:],
        }
        for idx_line in enumerate(
            [list(map(int, line.replace(":", "").split())) for line in values]
        )
    ]


def _get_possible_eqations(
    queue: list[dict], ops: list[Callable[[int, int], int]]
) -> int:
    done_dict = {}
    while queue:
        entry = queue.pop()
        if entry["equation_idx"] in done_dict:
            continue
        if not entry["remaining"]:
            if entry["current"] == entry["target"]:
                done_dict[entry["equation_idx"]] = entry["target"]
            continue
        queue.extend(
            [
                {
                    **entry,
                    "remaining": entry["remaining"][1:],
                    "current": op_result,
                }
                for op in ops
                if (op_result := op(entry["current"], entry["remaining"][0]))
                <= entry["target"]
            ]
        )
    return sum(done_dict.values())


test_config = {
    "input": """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
        "\n"
    ),
    "expected_solution_1": 3749,
    "expected_solution_2": 11387,
}
