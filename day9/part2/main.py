import os
from utils import find_basins


BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day9/part2/input'), "r") as f:
            lines = f.readlines()
            flow_map = []
            for line in lines:
                flow_map.append(line.strip())
            basins = find_basins(flow_map)
            basins.sort(reverse=True)
            print(basins[0] * basins[1] * basins[2])

    except FileNotFoundError:
        print(FileNotFoundError)


main()
