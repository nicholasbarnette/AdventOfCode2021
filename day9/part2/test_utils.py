import unittest
from utils import find_basins

# python -m unittest test_utils


class TestUtils(unittest.TestCase):

    def test_find_basins(self):
        self.assertEqual(find_basins(
            ["2199943210",
             "3987894921",
             "9856789892",
             "8767896789",
             "9899965678"]), [3, 9, 14, 9])


if __name__ == '__main__':
    unittest.main()
