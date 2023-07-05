import unittest

from pv import pv

class TestPresentValue(unittest.TestCase):

    def test_case1(self):
        future_value = 2000
        rate = 0.035
        n = 5
        expected = 1683.95
        self.assertAlmostEqual(expected, pv(future_value, rate, n), 2)


if __name__ == '__main__':
    unittest.main()
