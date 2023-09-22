import os
import sys

sys.path.insert(1, os.getcwd())

import unittest
from pin_generator.PinGenerator import PinGenerator

import util_test_functions


class MultiDigitGeneratorTest(unittest.TestCase):
    iterations = 1000  # Since output for functions is random, it is vital to run it over multiple iterations

    def test_correct_number_of_digits(self):
        num_digits = 6
        random_number = PinGenerator().generate_multi_digit_number(num_digits)
        self.assertEqual(num_digits, util_test_functions.count_number_of_digits(random_number))

    def test_no_repeating_consecutive_digits(self):
        num_digits = 6
        for i in range(self.iterations):
            random_number = PinGenerator().generate_multi_digit_number(num_digits)
            self.assertEqual(True, util_test_functions.check_no_same_consecutive_digits(random_number))

    def test_no_incremental_consecutive_digits(self):
        num_digits = 6
        for i in range(self.iterations):
            random_number = PinGenerator().generate_multi_digit_number(num_digits)
            self.assertEqual(True, util_test_functions.check_no_consecutive_incremental_digits(random_number))


if __name__ == '__main__':
    unittest.main()
