from functools import reduce
from time import time

from utils import open_file


def solution(values=open_file("4").split("\n")):
    a = time()
    solution_2(values)
    print(time() - a)
    return (solution_1(values), solution_2(values))


def solution_1(horizontals: list[str]):
    verticals = transpose_matrix(horizontals)
    diagonals = get_both_diagonals(verticals)
    return reduce(
        get_substr_occurrences,
        [*horizontals, *verticals, *diagonals[0], *diagonals[1]],
        0,
    )


def solution_2(lines: list[str]):
    total = 0
    for i in range(1, len(lines) - 1):
        a_idx = 1
        while -1 < a_idx < len(lines[i]) - 1:
            a_idx = lines[i].find("A", a_idx)
            if -1 < a_idx < len(lines[i]) - 1:
                x_line_1 = [
                    lines[i - 1][a_idx - 1],
                    lines[i + 1][a_idx + 1],
                ]
                x_line_2 = [
                    lines[i - 1][a_idx + 1],
                    lines[i + 1][a_idx - 1],
                ]
                if sorted(x_line_1) == ["M", "S"] and sorted(x_line_2) == ["M", "S"]:
                    total += 1
                a_idx += 1

    return total


def get_substr_occurrences(acc: int, string: str) -> int:
    count = 0
    for substr in ["XMAS", "SAMX"]:
        idx = 0
        while idx > -1:
            idx = string.find(substr, idx)
            if idx > -1:
                count += 1
                idx += 1
    return acc + count


def transpose_matrix(matrix: list[str]) -> list[str]:
    return ["".join(list(tuple)) for tuple in (zip(*reversed(matrix)))]


def get_both_diagonals(matrix: list[str]) -> list[list[str]]:
    diagonals = [
        [
            "".join(
                [
                    r[i + offset]
                    for i, r in enumerate(version)
                    if len(version[0]) > (i + offset) >= 0
                ]
            )
            for offset in range(len(version[0]) - 1, -len(version[0]), -1)
        ]
        for version in [matrix, list(reversed(matrix))]
    ]
    return diagonals


test_config = {
    "input": """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split(
        "\n"
    ),
    "expected_solution_1": 18,
    "expected_solution_2": 9,
}
