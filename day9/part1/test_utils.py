import unittest
from utils import find_low_points

# python -m unittest test_utils


class TestUtils(unittest.TestCase):

    def test_determine_output(self):
        self.assertEqual(find_low_points(
            ["2199943210",
             "3987894921",
             "9856789892",
             "8767896789",
             "9899965678"]), 15)


if __name__ == '__main__':
    unittest.main()
