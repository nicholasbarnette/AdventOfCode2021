import os
from utils import find_low_points


BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day9/part1/input'), "r") as f:
            lines = f.readlines()
            flow_map = []
            for line in lines:
                flow_map.append(line.strip())
            print(find_low_points(flow_map))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
