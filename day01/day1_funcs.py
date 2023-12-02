import re


def part1_transform_number(number_string):
    digits_only = re.sub(r"[a-zA-Z]", "", number_string)
    first_digit = digits_only[0]
    last_digit = digits_only[-1:]
    return int(first_digit + last_digit)


def part2_transform_number(number_string):
    looking_for = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    found = list()
    for f in looking_for.keys():
        indexes = [m.start() for m in re.finditer(f, number_string)]
        for i in indexes:
            found.append((f,i))

    sorted_found = sorted(found, key=lambda x: x[1])
    first = looking_for[sorted_found[0][0]]
    last = looking_for[sorted_found[-1][0]]
    return int(first+last)
