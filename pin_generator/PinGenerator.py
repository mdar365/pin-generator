from random import choice


class PinGenerator:
    def __init__(self):
        pass

    def generate_multi_digit_number(self, num_digits):
        previous_num = None
        incremental_warning = False
        digits = []
        for i in range(num_digits):
            random_digit = self.generate_digit(previous_num, incremental_warning)
            digits.append(random_digit)
            if previous_num is not None and random_digit == previous_num + 1:
                incremental_warning = True
            else:
                incremental_warning = False

            previous_num = random_digit

        return ''.join(map(str, digits))

    @staticmethod
    def generate_digit(previous_num, incremental_warning):
        numbers_to_exclude = []
        if previous_num is not None:
            numbers_to_exclude.append(previous_num)
            if incremental_warning:
                numbers_to_exclude.append(previous_num + 1)
        return choice([i for i in range(0, 10) if i not in numbers_to_exclude])

    def generate_pin_number(self):
        num_digits_in_pin = 4
        return self.generate_multi_digit_number(num_digits_in_pin)

    def generate_multiple_unique_pins(self, count):
        pins = []
        while len(pins) < count:
            pin = self.generate_pin_number()
            if pin not in pins:
                pins.append(pin)

        return pins

    def generate_thousand_unique_pins(self):
        num_pins = 1000
        return self.generate_multiple_unique_pins(num_pins)
