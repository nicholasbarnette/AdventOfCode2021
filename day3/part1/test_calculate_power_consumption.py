import unittest
from calculate_power_consumption import calculate_power_consumption

# python -m unittest test_calculate_power_consumption


class TestCalculatePowerConsumtion(unittest.TestCase):

    def test_calculate_power_consumption(self):
        self.assertEqual(calculate_power_consumption(
            ['00100',
             '11110',
             '10110',
             '10111',
             '10101',
             '01111',
             '00111',
             '11100',
             '10000',
             '11001',
             '00010',
             '01010']), ['10110', '01001'])


if __name__ == '__main__':
    unittest.main()
