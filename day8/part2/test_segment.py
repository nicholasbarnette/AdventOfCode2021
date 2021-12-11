import unittest
from segment import determine_output

# python -m unittest test_segment


class TestLanternFish(unittest.TestCase):

    def test_determine_output(self):
        self.assertEqual(determine_output(
            "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf\n"), "5353")
        self.assertEqual(determine_output(
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n"), "8394")
        self.assertEqual(determine_output(
            'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\n'), "9781")
        self.assertEqual(determine_output(
            'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\n'), "1197")


if __name__ == '__main__':
    unittest.main()
