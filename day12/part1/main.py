import os
from Map import Map


BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day12/part1/input'), "r") as f:
            lines = f.readlines()
            paths = []
            for line in lines:
                paths.append(line.strip())
            m = Map(paths)
            print(str(m))
            print(str(m.get_nodes()))
            print(len(m.find_paths()))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
