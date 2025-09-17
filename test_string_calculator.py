import unittest 
from string_calculator_TDD import add
class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""),0)
               