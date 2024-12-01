#!/usr/bin/env bash

NEW_FOLDER=day_$1
mkdir $NEW_FOLDER
cd $NEW_FOLDER
touch input
echo "from utils import open_file


def solution(values = open_file(\"$1\").split(\"\\n\")):
    solution_1 = solution_1(values)
    solution_2 = solution_2(values)
    return (solution_1, solution_2)


def solution_1(values: list[str]):
    return None


def solution_2(values: list[str]):
    return None

test_config = {
    \"input\": \"\"\"\"\"\".split(\"\n\"),
    \"expected_solution_1\": None,
    \"expected_solution_2\": None,
}
" >> main.py