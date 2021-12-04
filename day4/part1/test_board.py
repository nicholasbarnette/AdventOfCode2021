import unittest
from Board import Board

# python -m unittest test_board


class TestBoard(unittest.TestCase):

    def test_board_init(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ])
        self.assertEqual(str(
            board), '0\t1\t2\t3\t4\t\n5\t6\t7\t8\t9\t\n10\t11\t12\t13\t14\t\n15\t16\t17\t18\t19\t\n20\t21\t22\t23\t24\t\n')

    def test_check_for_win_horizontal(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ])
        self.assertEqual(board.check_for_win(), False)
        board.handle_numbers([0, 1, 2, 3, 4])
        self.assertEqual(board.check_for_win(), True)

    def test_check_for_win_vertical(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ])
        self.assertEqual(board.check_for_win(), False)
        board.handle_numbers([0, 5, 10, 15, 20])
        self.assertEqual(board.check_for_win(), True)


if __name__ == '__main__':
    unittest.main()
