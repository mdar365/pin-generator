import os
import sys

sys.path.insert(1, os.getcwd())

import unittest

from pin_generator.PinGenerator import PinGenerator
import util_test_functions


class PinGeneratorTest(unittest.TestCase):
    def test_correct_number_digits(self):
        pin = PinGenerator().generate_pin_number()
        self.assertEqual(4, util_test_functions.count_number_of_digits(pin))

    def test_correct_number_of_pins(self):
        num_pins = 5
        pins = PinGenerator().generate_multiple_unique_pins(num_pins)
        self.assertEqual(num_pins, len(pins))

    def test_all_pins_are_unique(self):
        num_pins = 1000
        pins = PinGenerator().generate_multiple_unique_pins(num_pins)
        unique_pins = list(set(pins))
        self.assertEqual(num_pins, len(unique_pins))

    def test_correct_number_for_thousand_pins_generator(self):
        pins = PinGenerator().generate_thousand_unique_pins()
        self.assertEqual(1000, len(pins))


if __name__ == '__main__':
    unittest.main()
