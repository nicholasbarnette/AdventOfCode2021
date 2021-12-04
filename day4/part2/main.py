import os
from Bingo import Bingo
import re

BASE_PATH = r'/Users/nickmac/Desktop/AdventOfCode2021'


def main():
    try:
        with open(os.path.join(BASE_PATH, './day4/part2/input'), "r") as f:
            lines = f.readlines()

            playable_numbers = lines[0].strip().split(',')
            game = Bingo()

            # Generate boards
            numbers = []
            i = 1
            while i < len(lines):
                line = lines[i]
                nums = re.split(r"\s+", line.strip())
                if len(nums) == 5:
                    numbers = numbers + nums

                if len(numbers) == 25:
                    game.add_board(numbers)
                    numbers = []

                i += 1

            # Play numbers
            last_winner = None
            last_number = None
            for num in playable_numbers:
                game.play_number(num)
                winners = game.check_boards_for_winners()
                winners.sort()
                winners.reverse()
                if len(winners) > 0:
                    last_number = int(num)
                    for w in winners:
                        last_winner = w

            # Calculate outcome
            cells = game.get_board(last_winner).get_cells()
            unchecked_cells_sum = 0
            for cell in cells:
                if cell.get_checked() == False:
                    unchecked_cells_sum += cell.get_number()
            print(unchecked_cells_sum, last_number)
            print(unchecked_cells_sum * last_number)

    except FileNotFoundError:
        print(FileNotFoundError)


main()
