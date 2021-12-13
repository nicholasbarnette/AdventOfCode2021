import os
import math
from utils import find_incomplete_lines, complete_lines


BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day10/part2/input'), "r") as f:
            lines = f.readlines()
            incomplete_lines = find_incomplete_lines(lines)
            print(complete_lines(incomplete_lines))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
