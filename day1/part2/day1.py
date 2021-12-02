import os

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def analyze_lines(lines):
    increaseCount = 0
    previousWindow = [0, 0, 0]
    currentWindow = [0, 0, 0]

    for idx, _ in enumerate(lines):
        # Get and parse the numbers for the window
        n1 = int(lines[idx]) if idx < len(
            lines) and lines[idx] != None else 0
        n2 = int(lines[idx+1]) if idx+1 < len(
            lines) and lines[idx+1] != None else 0
        n3 = int(lines[idx+2]) if idx + \
            2 < len(lines) and lines[idx+2] != None else 0

        # Create the current window
        currentWindow = [n1, n2, n3]

        if idx >= 1:
            # If the sum of the current window is greater than the previous window increase increaseCount
            if sum(currentWindow) > sum(previousWindow):
                increaseCount += 1

        # Set the current window to be the previous window
        previousWindow = currentWindow
    return increaseCount


def main():
    try:
        with open(os.path.join(BASE_PATH, './day1/part1/input'), "r") as f:
            lines = f.readlines()
            print(analyze_lines(lines))

    except FileNotFoundError:
        print(FileNotFoundError)


main()
