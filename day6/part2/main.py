import os
from LanternFishSchool import LanternFishSchool
import re

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day6/part1/input'), "r") as f:
            lines = f.readlines()
            fish = lines[0].split(',')
            school = LanternFishSchool(fish)
            prev_len = 0
            for i in range(256):
                school.elapse_day()
                print("Day %d: %d (%d)" %
                      (i, len(school) - prev_len, len(school)))
                prev_len = len(school)

            print(len(school))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
