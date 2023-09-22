def check_no_same_consecutive_digits(number):
    previous_char = None
    for char in str(number):
        if previous_char is not None and char == previous_char:
            return False
        previous_char = char

    return True


def check_no_consecutive_incremental_digits(number):
    previous_char = None
    incremental_warning = False
    for char in str(number):
        if previous_char is not None:
            if incremental_warning and int(char) == int(previous_char) + 1:
                return False
            elif not incremental_warning and int(char) == int(previous_char) + 1:
                incremental_warning = True
            else:
                incremental_warning = False

        previous_char = char

    return True


def count_number_of_digits(number):
    return len(str(number))
