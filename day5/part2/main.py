import os
from SurfaceMap import SurfaceMap
import re

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day5/part2/input'), "r") as f:
            lines = f.readlines()
            sm = SurfaceMap()
            for line in lines:
                sm.add_vent(line)

            danger_count = 0
            for c in str(sm):
                try:
                    if int(c) > 1:
                        danger_count += 1
                except:
                    continue
            print(danger_count)

    except FileNotFoundError:
        print(FileNotFoundError)


main()
