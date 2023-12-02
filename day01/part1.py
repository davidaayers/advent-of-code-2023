import re


def transform_number(number):
    digits_only = re.sub(r"[a-zA-Z]", "", number)
    first_digit = digits_only[0]
    last_digit = digits_only[-1:]
    return int(first_digit + last_digit)


def transform_numbers(numbers):
    return [transform_number(n) for n in numbers]


def sum_numbers(numbers):
    return sum(numbers)
