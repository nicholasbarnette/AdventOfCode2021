import unittest
from day1 import analyze_lines

# cd day1 && python -m unittest test_day1


class TestAnalyzeLines(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(analyze_lines([]), 0)

    def test_short_list(self):
        self.assertEqual(analyze_lines(["123\n"]), 0)

    def test_list_without_increases(self):
        self.assertEqual(analyze_lines(
            ["123\n", "122\n", "121\n", "120\n", "119\n"]), 0)

    def test_list_with_increases(self):
        self.assertEqual(analyze_lines(
            ["199\n", "200\n", "208\n", "210\n", "200\n", "207\n", "240\n", "269\n", "260\n", "263\n"]), 5)


if __name__ == '__main__':
    unittest.main()
