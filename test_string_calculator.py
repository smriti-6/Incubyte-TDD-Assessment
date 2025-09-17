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
    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)
    def test_negative_number_raises_exception(self):
        with self.assertRaises(Exception) as context:
          add("1,-2,3")
        self.assertEqual(str(context.exception),"negative numbers not allowed -2")

    def test_multiple_negative_numbers_raise_exception(self):
        with self.assertRaises(Exception) as context:
          add("-1,-2,3")
        self.assertEqual(str(context.exception),"negative numbers not allowed -1,-2")


    