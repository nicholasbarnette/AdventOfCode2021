import unittest
from Submarine import Submarine

# python -m unittest test_Submarine


class TestSubmarine(unittest.TestCase):

    def test_new_submarine(self):
        self.assertEqual(Submarine().get_position(), [0, 0])

    def test_depth(self):
        sub = Submarine()
        sub.move('down', 10)
        self.assertEqual(sub.get_position(), [0, 10])
        sub.move('up', 5)
        self.assertEqual(sub.get_position(), [0, 5])

    def test_horizontal(self):
        sub = Submarine()
        sub.move('forward', 10)
        self.assertEqual(sub.get_position(), [10, 0])

    def test_movement(self):
        sub = Submarine()
        sub.move('down', 10)
        self.assertEqual(sub.get_position(), [0, 10])
        sub.move('forward', 15)
        self.assertEqual(sub.get_position(), [15, 10])
        sub.move('up', 5)
        self.assertEqual(sub.get_position(), [15, 5])


if __name__ == '__main__':
    unittest.main()
