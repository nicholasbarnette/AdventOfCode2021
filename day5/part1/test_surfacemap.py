import unittest
from SurfaceMap import SurfaceMap

# python -m unittest test_surfacemap


class TestSurfaceMap(unittest.TestCase):

    def test_surfacemap_init(self):
        sm = SurfaceMap()
        self.assertEqual(len(sm), 0)

    def test_add_vent_horizontal(self):
        sm = SurfaceMap()
        sm.add_vent('0,0 -> 3,0')
        self.assertEqual(len(sm), 1)
        self.assertEqual(str(sm), '1111\n')
        sm.add_vent('2,0 -> 3,0')
        self.assertEqual(len(sm), 2)
        self.assertEqual(str(sm), '1122\n')
        sm.add_vent('2,1 -> 3,1')
        self.assertEqual(len(sm), 3)
        self.assertEqual(str(sm), '1122\n..11\n')

    def test_add_vent_vertical(self):
        sm = SurfaceMap()
        sm.add_vent('0,0 -> 0,3')
        self.assertEqual(len(sm), 1)
        self.assertEqual(str(sm), '1\n1\n1\n1\n')
        sm.add_vent('0,2 -> 0,3')
        self.assertEqual(len(sm), 2)
        self.assertEqual(str(sm), '1\n1\n2\n2\n')
        sm.add_vent('1,2 -> 1,3')
        self.assertEqual(len(sm), 3)
        self.assertEqual(str(sm), '1.\n1.\n21\n21\n')

    def test_add_vent_not_straight_line(self):
        sm = SurfaceMap()
        sm.add_vent('0,0 -> 1,1')
        self.assertEqual(len(sm), 0)

    def test_add_vent_vertical_and_horizontal(self):
        sm = SurfaceMap()
        sm.add_vent('0,0 -> 1,0')
        sm.add_vent('0,0 -> 0,1')
        self.assertEqual(len(sm), 2)
        self.assertEqual(str(sm), '21\n1.\n')

    def test_add_vents(self):
        sm = SurfaceMap()
        sm.add_vent('0,9 -> 5,9')
        sm.add_vent('8,0 -> 0,8')
        sm.add_vent('9,4 -> 3,4')
        sm.add_vent('2,2 -> 2,1')
        sm.add_vent('7,0 -> 7,4')
        sm.add_vent('6,4 -> 2,0')
        sm.add_vent('0,9 -> 2,9')
        sm.add_vent('3,4 -> 1,4')
        sm.add_vent('0,0 -> 8,8')
        sm.add_vent('5,5 -> 8,2')
        self.assertEqual(len(sm), 6)
        self.assertEqual(str(
            sm), '.......1..\n..1....1..\n..1....1..\n.......1..\n.112111211\n..........\n..........\n..........\n..........\n222111....\n')


if __name__ == '__main__':
    unittest.main()
