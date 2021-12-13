import os
from Grid import Grid


BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day11/part1/input'), "r") as f:
            lines = f.readlines()
            octopi = []
            for line in lines:
                for o in line.strip():
                    octopi.append(o)
            g = Grid(octopi)
            for _ in range(100):
                g.step()
            print(g.get_flashes())

    except FileNotFoundError:
        print(FileNotFoundError)


main()
