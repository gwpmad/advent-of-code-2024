from utils import open_file


def solution(values=open_file("6").split("\n")):
    return (solution_1(values), solution_2(values))


def solution_1(values: list[str]):
    lambda_idx = 0
    y, x = _get_start(values)

    lambdas = [
        lambda y, x: (y - 1, x),
        lambda y, x: (y, x + 1),
        lambda y, x: (y + 1, x),
        lambda y, x: (y, x - 1),
    ]
    visited = set[str]()
    while True:
        visited.add(f"{y},{x}")
        old_y, old_x = y, x
        y, x = lambdas[lambda_idx](y, x)

        if (0 <= y < len(values)) and (0 <= x < len(values[0])):
            if values[y][x] == "#":
                y, x = old_y, old_x
                lambda_idx = (lambda_idx + 1) % len(lambdas)
                continue
        else:
            break

    return len(visited)


def solution_2(values: list[str]):
    values_list = [list(value) for value in values]
    original_y, original_x = _get_start(values)

    lambdas = [
        lambda y, x: (y - 1, x),
        lambda y, x: (y, x + 1),
        lambda y, x: (y + 1, x),
        lambda y, x: (y, x - 1),
    ]
    total = 0
    for post_y in range(0, len(values)):
        for post_x in range(0, len(values[0])):
            if values_list[post_y][post_x] != ".":
                continue
            values_list[post_y][post_x] = "#"

            y, x = original_y, original_x
            visited_directions = set[str]()
            lambda_idx = 0
            while True:
                place_direction = f"{y},{x},{lambda_idx}
                if place_direction in visited_directions:
                    total += 1
                    break
                visited_directions.add(place_direction)

                old_y, old_x = y, x
                y, x = lambdas[lambda_idx](y, x)

                if (0 <= y < len(values_list)) and (0 <= x < len(values_list[0])):
                    if values_list[y][x] == "#":
                        y, x = old_y, old_x
                        lambda_idx = (lambda_idx + 1) % len(lambdas)
                        continue
                else:
                    break
            values_list[post_y][post_x] = "."

    return total


def _get_start(values: list[str]) -> tuple[int, int]:
    for i, row in enumerate(values):
        if "^" in row:
            y, x = i, row.index("^")
            break
    return (y, x)


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
    "expected_solution_2": 6,
}
