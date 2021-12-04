import unittest
from calculate_life_support_rating import calculate_life_support_rating

# python -m unittest test_calculate_life_support_rating


class TestCalculateLifeSupportRatings(unittest.TestCase):

    def test_calculate_life_support_rating(self):
        self.assertEqual(calculate_life_support_rating(
            ['00100',
             '11110',
             '10110',
             '10111',
             '10101',
             '01111',
             '00111',
             '11100',
             '10000',
             '11001',
             '00010',
             '01010']), [23, 10])


if __name__ == '__main__':
    unittest.main()
