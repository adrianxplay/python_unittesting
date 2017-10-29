import unittest
from curp_calculator import calculator

class TestCurpCalculator(unittest.TestCase):
    def setUp(self):
        pass

    def test_adrian(self):
        self.assertEqual(calculator("", "", "", "", "h"), "")

if __name__ == "__main__":
    unittest.main()