import unittest
from utils import find_median, calculate_fuel_usage

# python -m unittest test_utils


class TestLanternFish(unittest.TestCase):

    def test_find_median(self):
        self.assertEqual(find_median([0]), 0)
        self.assertEqual(find_median([0, 1]), 1)
        self.assertEqual(find_median([0, 1, 2]), 1)
        self.assertEqual(find_median([0, 1, 2, 3]), 2)

    def test_calculate_fuel_usage(self):
        self.assertEqual(calculate_fuel_usage([0], 0), 0)
        self.assertEqual(calculate_fuel_usage([0, 1], 1), 1)
        self.assertEqual(calculate_fuel_usage([0, 1, 2], 1), 2)
        self.assertEqual(calculate_fuel_usage([0, 1, 2, 3], 2), 4)
        self.assertEqual(calculate_fuel_usage([0, 1, 2, 3, 4], 2), 6)
        self.assertEqual(calculate_fuel_usage(
            [16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 2), 37)
        self.assertEqual(calculate_fuel_usage(
            [16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 1), 41)
        self.assertEqual(calculate_fuel_usage(
            [16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 3), 39)
        self.assertEqual(calculate_fuel_usage(
            [16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 10), 71)


if __name__ == '__main__':
    unittest.main()
