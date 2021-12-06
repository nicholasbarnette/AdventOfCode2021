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
        s.elapse_day()
        self.assertEqual(len(s), 4)
        self.assertEqual(s.get_school()[3].get_spawn_timer(), 8)
        s.elapse_day()
        self.assertEqual(len(s), 5)
        s.elapse_day()
        self.assertEqual(len(s), 6)

    def test_create_spawn(self):
        s = LanternFishSchool(['0'])
        s.elapse_day()
        self.assertEqual(len(s), 2)
        self.assertEqual(s.get_school()[1].get_spawn_timer(), 8)


if __name__ == '__main__':
    unittest.main()
