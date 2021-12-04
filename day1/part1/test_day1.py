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
            ["123\n", "124\n", "125\n", "126\n", "127\n"]), 4)
        self.assertEqual(analyze_lines(
            ["123\n", "124\n", "122\n", "126\n", "127\n"]), 3)


if __name__ == '__main__':
    unittest.main()
