import os
from Grid import Grid


BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day11/part2/input'), "r") as f:
            lines = f.readlines()
            octopi = []
            for line in lines:
                for o in line.strip():
                    octopi.append(o)
            g = Grid(octopi)

            first_sync = -1
            while first_sync == -1:
                g.step()
                synced = True
                for r in g.get_grid():
                    for c in r:
                        if c.get_energy() != 0:
                            synced = False
                if synced == True:
                    first_sync = g.get_steps

            print(g.get_steps(), g.get_flashes())

    except FileNotFoundError:
        print(FileNotFoundError)


main()
