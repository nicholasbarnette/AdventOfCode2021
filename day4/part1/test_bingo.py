import unittest
import random
from Bingo import Bingo

# python -m unittest test_bingo


class TestBoard(unittest.TestCase):

    def test_bingo_init(self):
        game = Bingo()
        self.assertEqual(len(game), 0)
        game.add_board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
        game.add_board([random.randint(0, 150) for n in range(25)])
        game.add_board([random.randint(0, 150) for n in range(25)])
        self.assertEqual(len(game), 3)

    def test_bingo_for_winner_horizontal(self):
        game = Bingo()
        game.add_board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ])
        game.add_board([random.randint(0, 150)] * 25)
        game.add_board([random.randint(0, 150)] * 25)
        self.assertEqual(game.check_boards_for_winners(), [])
        game.play_number(0)
        game.play_number(1)
        game.play_number(2)
        game.play_number(3)
        game.play_number(4)
        self.assertEqual(game.check_boards_for_winners(), [0])

    def test_bingo_for_winner_vertical(self):
        game = Bingo()
        game.add_board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ])
        game.add_board([random.randint(0, 150)] * 25)
        game.add_board([random.randint(0, 150)] * 25)
        self.assertEqual(game.check_boards_for_winners(), [])
        game.play_number(0)
        game.play_number(5)
        game.play_number(10)
        game.play_number(15)
        game.play_number(20)
        self.assertEqual(game.check_boards_for_winners(), [0])


if __name__ == '__main__':
    unittest.main()
