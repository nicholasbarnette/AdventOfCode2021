import os
from calculate_life_support_rating import calculate_life_support_rating

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day3/part2/input'), "r") as f:
            lines = f.readlines()
            [o2gen, co2scrubber] = (calculate_life_support_rating(lines))
            print(o2gen * co2scrubber)

    except FileNotFoundError:
        print(FileNotFoundError)


main()
