from Submarine import Submarine
import os

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    sub = Submarine()

    try:
        with open(os.path.join(BASE_PATH, './day2/part2/input'), "r") as f:
            lines = f.readlines()

            for l in lines:
                [direction, units] = (l.split(' '))
                sub.move(direction, int(units))

            [x, y] = (sub.get_position())
            print(x * y)

    except FileNotFoundError:
        print(FileNotFoundError)


main()
