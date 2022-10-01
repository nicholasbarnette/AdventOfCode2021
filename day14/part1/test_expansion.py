import unittest
from Expansion import Expansion

# python -m unittest test_expansion


class TestExpansion(unittest.TestCase):

    def test_expansion_simulate(self):
        e = Expansion('NNCB', [['CH', 'B'],
                               ['HH', 'N'],
                               ['CB', 'H'],
                               ['NH', 'C'],
                               ['HB', 'C'],
                               ['HC', 'B'],
                               ['HN', 'C'],
                               ['NN', 'C'],
                               ['BH', 'H'],
                               ['NC', 'B'],
                               ['NB', 'B'],
                               ['BN', 'B'],
                               ['BB', 'N'],
                               ['BC', 'B'],
                               ['CC', 'N'],
                               ['CN', 'C']])
        self.assertEqual(str(e), 'NNCB')
        self.assertEqual(e.find_character_prevalence(),
                         {'N': 2, 'C': 1, "B": 1})
        self.assertEqual(e.simulate(), 'NCNBCHB')
        self.assertEqual(e.find_character_prevalence(),
                         {'N': 2, 'C': 2, "B": 2, "H": 1})
        self.assertEqual(e.simulate(), 'NBCCNBBBCBHCB')
        self.assertEqual(e.find_character_prevalence(),
                         {'N': 2, 'C': 4, "B": 6, "H": 1})
        self.assertEqual(e.simulate(), 'NBBBCNCCNBBNBNBBCHBHHBCHB')
        self.assertEqual(e.find_character_prevalence(),
                         {'N': 5, 'C': 5, "B": 11, "H": 4})
        self.assertEqual(
            e.simulate(), 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')
        self.assertEqual(e.find_character_prevalence(),
                         {'N': 11, 'C': 10, "B": 23, "H": 5})


if __name__ == '__main__':
    unittest.main()
