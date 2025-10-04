import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-5, 10), 5)
        self.assertEqual(self.calc.add(0, 7), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(0, 8), -8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, -2), -10)
        self.assertEqual(self.calc.multiply(-6, -3), 18)
        self.assertEqual(self.calc.multiply(99, 0), 0)

    def test_divide(self):
        # Integer result - Use assertEqual
        self.assertEqual(self.calc.divide(10, 2), 5)
        
        # Float result - MUST use assertAlmostEqual for reliable comparison
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5) 
        
        self.assertEqual(self.calc.divide(-15, 3), -5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Division by zero edge case
        self.assertIsNone(self.calc.divide(10, 0))

if _name_ == '_main_':
    unittest.main()