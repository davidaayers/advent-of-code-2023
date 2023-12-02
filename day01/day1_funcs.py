import re


def part1_transform_number(number):
    digits_only = re.sub(r"[a-zA-Z]", "", number)
    first_digit = digits_only[0]
    last_digit = digits_only[-1:]
    return int(first_digit + last_digit)

