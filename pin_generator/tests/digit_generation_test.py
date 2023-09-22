import os
import sys

sys.path.insert(1, os.getcwd())

import unittest
from scipy.stats import chisquare
from collections import Counter

from pin_generator.PinGenerator import PinGenerator


class DigitGeneratorTest(unittest.TestCase):
    iterations = 1000  # Since output for functions is random, it is vital to run it over multiple iterations

    def test_not_producing_same_digit(self):
        previous_number = 2
        incremental_warning = False
        for i in range(self.iterations):
            random_digit = PinGenerator.generate_digit(previous_number, incremental_warning)
            self.assertNotEqual(random_digit, previous_number)

    def test_if_incremental_warning(self):
        previous_number = 2
        incremental_warning = True
        for i in range(self.iterations):
            random_digit = PinGenerator.generate_digit(previous_number, incremental_warning)
            self.assertNotEqual(random_digit, previous_number + 1)

    def test_numbers_within_range(self):
        previous_number = None
        incremental_warning = False
        for i in range(self.iterations):
            random_digit = PinGenerator.generate_digit(previous_number, incremental_warning)
            self.assertLess(random_digit, 10)
            self.assertGreaterEqual(random_digit, 0)

    def test_all_digits_produced_at_least_once(self):
        previous_number = None
        incremental_warning = False
        random_digit_range = range(0, 10)
        digits_possible = [i for i in random_digit_range]
        for i in range(self.iterations):
            random_digit = PinGenerator.generate_digit(previous_number, incremental_warning)
            if random_digit in digits_possible:
                digits_possible.remove(random_digit)

        self.assertEqual(len(digits_possible), 0)

    # Statistical test to test how random the generation is
    def test_randomness(self):
        previous_number = None
        incremental_warning = False

        digits = [PinGenerator.generate_digit(previous_number, incremental_warning) for _ in range(self.iterations)]

        # Count the occurrences of each digit
        digit_counts = dict(Counter(digits))

        # Expected frequency for each digit (assuming uniform distribution)
        expected_freq = self.iterations / 10

        # Observed frequencies of digits
        observed_freq = [digit_counts.get(i, 0) for i in range(10)]

        # Perform the chi-squared test
        chi2, p_value = chisquare(observed_freq, f_exp=expected_freq)

        # Check if the p-value is greater than a significance level (e.g., 0.05)
        self.assertGreater(p_value, 0.05)


if __name__ == '__main__':
    unittest.main()
