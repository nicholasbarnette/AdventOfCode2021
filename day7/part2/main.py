import os
from utils import find_mean, calculate_fuel_usage
import re

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day7/part2/input'), "r") as f:
            lines = f.readlines()
            positions = lines[0].split(',')

            print(len(positions))
            for idx, p in enumerate(positions):
                positions[idx] = int(p)

            mean = find_mean(positions)
            print(mean, calculate_fuel_usage(positions, mean))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
