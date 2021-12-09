import unittest
from utils import find_mean, calculate_fuel_usage

# python -m unittest test_utils


class TestLanternFish(unittest.TestCase):

    def test_find_mean(self):
        self.assertEqual(find_mean([0]), 0)
        self.assertEqual(find_mean([0, 1]), 0)
        self.assertEqual(find_mean([0, 1, 2]), 1)
        self.assertEqual(find_mean([0, 1, 2, 3]), 1)
        self.assertEqual(find_mean([0, 1, 2, 3, 4, 5, 6]), 3)

    def test_calculate_fuel_usage(self):
        self.assertEqual(calculate_fuel_usage([0], 0), 0)
        self.assertEqual(calculate_fuel_usage([0, 1], 0), 1)
        self.assertEqual(calculate_fuel_usage([0, 1, 2], 1), 2)
        self.assertEqual(calculate_fuel_usage([0, 1, 2, 3], 1), 5)
        self.assertEqual(calculate_fuel_usage([0, 1, 2, 3, 4], 2), 8)
        self.assertEqual(calculate_fuel_usage(
            [16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 5), 168)
        self.assertEqual(calculate_fuel_usage(
            [16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 2), 206)


if __name__ == '__main__':
    unittest.main()
