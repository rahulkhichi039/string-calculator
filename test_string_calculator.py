import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number_returns_itself(self):
        self.assertEqual(self.calculator.add("5"), 5)

    def test_two_numbers_return_sum(self):
        self.assertEqual(self.calculator.add("3,5"), 8)

    def test_multiple_numbers_return_sum(self):
        self.assertEqual(self.calculator.add("1,2,3,4,5"), 15)

    def test_newline_between_numbers_is_handled(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_different_delimiter_is_supported(self):
        self.assertEqual(self.calculator.add("//;\n4;6"), 10)

    def test_negative_number_throws_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1")
        self.assertIn("Negative numbers not allowed", str(context.exception))

    def test_multiple_negative_numbers_throw_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1,-2,-3")
        self.assertIn("Negative numbers not allowed", str(context.exception))
        self.assertIn("[-1, -2, -3]", str(context.exception))

    def test_numbers_greater_than_1000_are_ignored(self):
        self.assertEqual(self.calculator.add("1001,2"), 2)

    def test_long_custom_delimiter_is_supported(self):
        self.assertEqual(self.calculator.add("//[***]\n1***2***3"), 6)

    def test_multiple_custom_delimiters_are_supported(self):
        self.assertEqual(self.calculator.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_custom_delimiters_with_different_lengths(self):
        self.assertEqual(self.calculator.add("//[***][%%]\n3***4%%3"), 10)

    def test_numbers_greater_than_1000_ignored_with_multiple_delimiters(self):
        self.assertEqual(self.calculator.add("//[*][%]\n1*1001%2"), 3)

    def test_custom_delimiter_with_special_characters(self):
        self.assertEqual(self.calculator.add("//[$#]\n1$#2$#3"), 6)

if __name__ == '__main__':
    unittest.main()
