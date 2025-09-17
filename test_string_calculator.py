import unittest 
from string_calculator_TDD import add
class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""),0)
    def test_single_number(self):
        self.assertEqual(add("5"),5) 
    def test_two_numbers_sum(self):
        self.assertEqual(add("1,2"),3)      
    def test_newline_delimiter(self):
        self.assertEqual(add("1,\n2,3"),6)