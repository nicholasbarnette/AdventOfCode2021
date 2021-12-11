import os
from segment import determine_output


BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day8/part2/input'), "r") as f:
            lines = f.readlines()
            n = 0
            for line in lines:
                n += int(determine_output(line))
            print(n)

    except FileNotFoundError:
        print(FileNotFoundError)


main()
