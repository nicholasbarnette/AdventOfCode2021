import unittest
from LanternFishSchool import LanternFishSchool

# python -m unittest test_lanternfishschool


class TestLanternFish(unittest.TestCase):

    def test_lanternfish_init(self):
        s = LanternFishSchool(['0', '1', '2'])
        self.assertEqual(len(s), 3)

    def test_elapse_day(self):
        s = LanternFishSchool(['0', '1', '2'])
        self.assertEqual(len(s), 3)
        self.assertEqual(s.get_school(), [1, 1, 1, 0, 0, 0, 0, 0, 0])
        s.elapse_day()
        self.assertEqual(len(s), 4)
        self.assertEqual(s.get_school(), [1, 1, 0, 0, 0, 0, 1, 0, 1])
        s.elapse_day()
        self.assertEqual(len(s), 5)
        self.assertEqual(s.get_school(), [1, 0, 0, 0, 0, 1, 1, 1, 1])
        s.elapse_day()
        self.assertEqual(len(s), 6)
        self.assertEqual(s.get_school(), [0, 0, 0, 0, 1, 1, 2, 1, 1])
        s.elapse_day()
        s.elapse_day()
        s.elapse_day()
        s.elapse_day()
        self.assertEqual(len(s), 6)
        self.assertEqual(s.get_school(), [1, 1, 2, 1, 1, 0, 0, 0, 0])
        s.elapse_day()
        self.assertEqual(len(s), 7)
        self.assertEqual(s.get_school(), [1, 2, 1, 1, 0, 0, 1, 0, 1])
        s.elapse_day()
        self.assertEqual(len(s), 8)
        self.assertEqual(s.get_school(), [2, 1, 1, 0, 0, 1, 1, 1, 1])
        s.elapse_day()
        self.assertEqual(len(s), 10)
        self.assertEqual(s.get_school(), [1, 1, 0, 0, 1, 1, 3, 1, 2])

    def test_create_spawn(self):
        s = LanternFishSchool(['0'])
        self.assertEqual(len(s), 1)
        s.elapse_day()
        self.assertEqual(len(s), 2)
        self.assertEqual(s.get_school(), [0, 0, 0, 0, 0, 0, 1, 0, 1])

    def test_sim_80days(self):
        s = LanternFishSchool(['0'])
        for _ in range(80):
            s.elapse_day()
        self.assertEqual(len(s), 1421)

    def test_sim_256days(self):
        s = LanternFishSchool(['3', '4', '3', '1', '2'])
        for _ in range(256):
            s.elapse_day()
        self.assertEqual(len(s), 26984457539)


if __name__ == '__main__':
    unittest.main()
