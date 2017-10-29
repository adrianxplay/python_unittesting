import unittest
from unnecesary_math import multiply
from unnecesary_math import  divide


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_number_3_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')

    def test_number_3_3(self):
        self.assertEqual(multiply(3, 3), 9)

    def test_strings_3_a(self):
        self.assertEqual(multiply(3, 'a'), 'aaa')

    def test_0_0(self):
        self.assertRaises(ArithmeticError, divide, 1, 0)

if __name__ == '__main__':
    unittest.main()