import os
from calculate_power_consumption import calculate_power_consumption

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day3/part1/input'), "r") as f:
            lines = f.readlines()
            [gamma, epsilon] = calculate_power_consumption(lines)
            print(gamma, epsilon)
            print(int(gamma, base=2), int(epsilon, base=2))
            print(int(gamma, base=2) * int(epsilon, base=2))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
