import os
from utils import parse_syntax


BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day10/part1/input'), "r") as f:
            lines = f.readlines()
            error_sum = 0
            for line in lines:
                error_sum += parse_syntax(line)

            print(error_sum)

    except FileNotFoundError:
        print(FileNotFoundError)


main()
