import os
import re
from Paper import Paper

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day13/part1/input'), "r") as f:
            lines = f.readlines()
            points = []
            folds = []
            for line in lines:
                l = line.strip()
                if l == '':
                    continue
                res = re.findall(r'fold along (x|y)=(\d+)', l)
                res = res[0] if res else None
                if res:
                    if res[0] == 'x':
                        folds.append([int(res[1]), 0])
                    else:
                        folds.append([0, int(res[1])])
                else:
                    p = l.split(',')
                    points.append([int(p[0]), int(p[1])])

            print(folds)
            p = Paper(points)
            print(p.get_visible_dots())
            for f in folds:
                print(f, p.get_visible_dots())
                p.fold(f)
                print(f, p.get_visible_dots())
            print(str(p))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
