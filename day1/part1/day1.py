import os

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def analyze_lines(lines):
    increaseCount = 0
    for idx, _ in enumerate(lines):
        if idx >= 1:
            # If the current line is greater than the previous add to increaseCount
            if int(lines[idx]) > int(lines[idx-1]):
                increaseCount += 1
    return increaseCount


def main():
    try:
        with open(os.path.join(BASE_PATH, './day1/part1/input'), "r") as f:
            lines = f.readlines()
            print(analyze_lines(lines))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
