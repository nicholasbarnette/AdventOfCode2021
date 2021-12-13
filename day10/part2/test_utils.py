import unittest
from utils import parse_syntax, complete_line, complete_lines, find_incomplete_lines

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

    def test_find_incomplete_lines(self):
        self.assertEqual(find_incomplete_lines(['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(',
                         '(((({<>}<{<{<>}{[]{[]{}', '{<[[]]>}<{[{[{[]{()[[[]', '<{([{{}}[<[[[<>{}]]]>[]]']), ['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(',
                         '(((({<>}<{<{<>}{[]{[]{}', '{<[[]]>}<{[{[{[]{()[[[]', '<{([{{}}[<[[[<>{}]]]>[]]'])
        self.assertEqual(find_incomplete_lines(['{([(<{}[<>[]}>{[]{[(<()>', '[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(',
                         '(((({<>}<{<{<>}{[]{[]{}', '{<[[]]>}<{[{[{[]{()[[[]', '<{([{{}}[<[[[<>{}]]]>[]]']), ['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(',
                         '(((({<>}<{<{<>}{[]{[]{}', '{<[[]]>}<{[{[{[]{()[[[]', '<{([{{}}[<[[[<>{}]]]>[]]'])

    def test_complete_line(self):
        self.assertEqual(complete_line('[({(<(())[]>[[{[]{<()<>>'), 288957)
        self.assertEqual(complete_line('[(()[<>])]({[<{<<[]>>('), 5566)
        self.assertEqual(complete_line('(((({<>}<{<{<>}{[]{[]{}'), 1480781)
        self.assertEqual(complete_line('{<[[]]>}<{[{[{[]{()[[[]'), 995444)
        self.assertEqual(complete_line('<{([{{}}[<[[[<>{}]]]>[]]'), 294)

    def test_complete_lines(self):
        self.assertEqual(complete_lines(['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(',
                         '(((({<>}<{<{<>}{[]{[]{}', '{<[[]]>}<{[{[{[]{()[[[]', '<{([{{}}[<[[[<>{}]]]>[]]']), 288957)


if __name__ == '__main__':
    unittest.main()
