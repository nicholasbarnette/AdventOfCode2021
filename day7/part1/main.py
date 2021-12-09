import os
from utils import find_median, calculate_fuel_usage
import re

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day7/part1/input'), "r") as f:
            lines = f.readlines()
            positions = lines[0].split(',')
            print(len(positions))
            for idx, p in enumerate(positions):
                positions[idx] = int(p)
            median = find_median(positions)
            print(calculate_fuel_usage(positions, median))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
