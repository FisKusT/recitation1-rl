import unittest
from logic import CalculatorLogic

class TestCalculatorLogic(unittest.TestCase):
    def setUp(self):
        self.logic = CalculatorLogic()

    def test_basic_arithmetic(self):
        self.assertEqual(self.logic.calculate("5+5"), 10)
        self.assertEqual(self.logic.calculate("10-3"), 7)
        self.assertEqual(self.logic.calculate("4*3"), 12)
        self.assertEqual(self.logic.calculate("20/5"), 4)

    def test_advanced_operations(self):
        self.assertEqual(self.logic.calculate("2^3"), 8)
        self.assertEqual(self.logic.calculate("math.sqrt(16)"), 4)
        self.assertEqual(self.logic.calculate("1/4"), 0.25)

    def test_error_handling(self):
        self.assertEqual(self.logic.calculate("5/0"), "Error: Div by 0")
        self.assertEqual(self.logic.calculate("invalid"), "Error")

    def test_history(self):
        self.logic.calculate("1+1")
        self.logic.calculate("2+2")
        history = self.logic.get_history()
        self.assertIn("1+1 = 2", history)
        self.assertIn("2+2 = 4", history)

if __name__ == "__main__":
    unittest.main()
