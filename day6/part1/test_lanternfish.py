import unittest
from LanternFish import LanternFish

# python -m unittest test_lanternfish


class TestLanternFish(unittest.TestCase):

    def test_lanternfish_init(self):
        f = LanternFish(3)
        self.assertEqual(f.get_spawn_timer(), 3)

    def test_elapse_day(self):
        f = LanternFish(3)
        self.assertEqual(f.get_spawn_timer(), 3)
        self.assertFalse(f.elapse_day())
        self.assertEqual(f.get_spawn_timer(), 2)
        self.assertFalse(f.elapse_day())
        self.assertFalse(f.elapse_day())
        self.assertTrue(f.elapse_day())
        self.assertEqual(f.get_spawn_timer(), 6)


if __name__ == '__main__':
    unittest.main()
