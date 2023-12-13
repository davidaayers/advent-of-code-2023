import re
import functools


def parse_input(input_lines):
    rows = []
    for line in input_lines:
        parts = line.split()
        spring_row = SpringRow()
        # remove repeating ".", they aren't necessary
        spring = re.sub(r"\.+", ".", parts[0])
        spring_row.springs = spring
        spring_row.how_many = [int(part) for part in parts[1].split(",")]
        rows.append(spring_row)

    return rows


@functools.cache
def find_num_permutations(spring_row, how_many, count):
    # print(f"{indent}row: '{spring_row}' how_many={how_many} count={count}")

    if len(how_many) == 0 and len(spring_row) > 0:
        # we don't have any more matching groups, but we have text left
        # that's ok if they are all ? or .
        for i in spring_row:
            if i != "?" and i != '.':
                return count

        # it was only ?, it's a match!
        # print(f"{indent}----> Found a match!")
        count += 1
        return count

    if len(spring_row) == 0:
        if len(how_many) == 0:
            # print(f"{indent}----> Found a match!")
            count += 1
        return count

    if spring_row[0] == ".":
        count = find_num_permutations(spring_row[1:], how_many, count)

    if spring_row[0] == "?":
        count = find_num_permutations("." + spring_row[1:], how_many, count)
        count = find_num_permutations("#" + spring_row[1:], how_many, count)

    if spring_row[0] == "#":
        length = how_many[0]
        found_match = True
        if len(spring_row) < length:
            found_match = False
        else:
            for i in range(length):
                c1 = spring_row[i]
                if c1 == ".":
                    found_match = False
                    break

        # make sure there isn't another # after this match, it must be a ? or a . or the end of line
        if len(spring_row) > length:
            next_char_after_match = spring_row[length]
            if next_char_after_match == "#":
                found_match = False
            else:
                # expand length to chop the next character too
                length += 1

        if found_match:
            new_string = spring_row[length:]
            count = find_num_permutations(new_string, how_many[1:], count)

    return count


class SpringRow:

    def __init__(self):
        self.springs = None
        self.how_many = None

    def __str__(self):
        return f"{self.springs}: {self.how_many}"
