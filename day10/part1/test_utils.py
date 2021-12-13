import unittest
from utils import parse_syntax

# python -m unittest test_utils


class TestUtils(unittest.TestCase):

    def test_parse_syntax(self):
        self.assertEqual(parse_syntax('()'), 0)
        self.assertEqual(parse_syntax('(<{[]}>)'), 0)
        self.assertEqual(parse_syntax('(()()(()))'), 0)

        self.assertEqual(parse_syntax('{([(<{}[<>[]}>{[]{[(<()>'), 1197)
        self.assertEqual(parse_syntax('[[<[([]))<([[{}[[()]]]'), 3)
        self.assertEqual(parse_syntax('[{[{({}]{}}([{[{{{}}([]'), 57)
        self.assertEqual(parse_syntax('[<(<(<(<{}))><([]([]()'), 3)
        self.assertEqual(parse_syntax('<{([([[(<>()){}]>(<<{{'), 25137)


if __name__ == '__main__':
    unittest.main()
