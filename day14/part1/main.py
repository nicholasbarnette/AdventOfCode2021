import os
import re
from Expansion import Expansion

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day14/part1/input'), "r") as f:
            lines = f.readlines()
            origin = lines[0].strip()
            mappings = []
            for line in lines:
                l = line.strip()
                l = re.findall(r'([A-Z]{2}) -> ([A-Z])', l)
                if len(l) == 1:
                    mappings.append([l[0][0], l[0][1]])
            e = Expansion(origin, mappings)

            # Simulate 10 times
            for _ in range(40):
                print(_)
                e.simulate()

            print(e.find_character_prevalence())

            prevalence = e.find_character_prevalence()
            min_prev = prevalence[origin[0]]
            max_prev = prevalence[origin[0]]
            for k, v in prevalence.items():
                min_prev = min(min_prev, v)
                max_prev = max(max_prev, v)

            print(min_prev, max_prev, max_prev - min_prev)
    except FileNotFoundError:
        print(FileNotFoundError)


main()
