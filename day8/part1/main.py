import os
import re

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def get_unique_values(lines):
    unique_values = 0
    for l in lines:
        output_values = l.split(' | ')[1].split(' ')
        for idx, v in enumerate(output_values):
            output_values[idx] = v.strip()

        for v in output_values:

            if len(v) == 2:
                # Found a 1
                unique_values += 1
            elif len(v) == 3:
                # Found a 7
                unique_values += 1
            elif len(v) == 4:
                # Found a 4
                unique_values += 1
            elif len(v) == 7:
                # Found a 8
                unique_values += 1
    return unique_values


def main():
    try:
        with open(os.path.join(BASE_PATH, './day8/part1/input'), "r") as f:
            lines = f.readlines()
            print(get_unique_values(lines))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
