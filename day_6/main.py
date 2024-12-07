from utils import open_file


def solution(values=open_file("6").split("\n")):
    return (solution_1(values), solution_2(values))


def solution_1(values: list[str]):
    y, x, lambda_idx = 0, 0, 0
    for i, row in enumerate(values):
        if "^" in row:
            y, x = i, row.index("^")
            break

    lambdas = [
        lambda y, x: (y - 1, x),
        lambda y, x: (y, x + 1),
        lambda y, x: (y + 1, x),
        lambda y, x: (y, x - 1),
    ]
    within_range = lambda y, x: (0 <= y < len(values)) and (0 <= x < len(values[0]))
    visited = {f"{y},{x}"}
    while within_range(y, x):
        old_y, old_x = y, x
        y, x = lambdas[lambda_idx](y, x)

        if within_range(y, x):
            if values[y][x] == "#":
                y, x = old_y, old_x
                lambda_idx = (lambda_idx + 1) % len(lambdas)
                continue
            visited.add(f"{y},{x}")

    return len(visited)


def solution_2(values: list[str]):
    return None


test_config = {
    "input": """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split(
        "\n"
    ),
    "expected_solution_1": 41,
    "expected_solution_2": None,
}
