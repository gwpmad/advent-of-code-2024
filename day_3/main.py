import re
from functools import reduce
from math import prod

from utils import open_file


def solution(values=open_file("3")):
    return (solution_1(values), solution_2(values))


def solution_1(value: str):
    ops = re.findall(r"(?<=mul\()\d+,\d+(?=\))", value)
    return reduce(lambda acc, mul: acc + prod(map(int, mul.split(","))), ops, 0)


def solution_2(value: str) -> int:
    ops = re.findall(r"do\(\)|don't\(\)|(?<=mul\()\d+,\d+(?=\))", value)
    return reduce(sum_enabled_muls, ops, {"do": True, "sum": 0})["sum"]


def sum_enabled_muls(acc, op):
    if op[0] == "d":
        acc["do"] = op == "do()"
    elif acc["do"]:
        acc["sum"] += prod(map(int, op.split(",")))
    return acc


test_config = {
    "input": "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
    "expected_solution_1": 161,
    "expected_solution_2": 48,
}
