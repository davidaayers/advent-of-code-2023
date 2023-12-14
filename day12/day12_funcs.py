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
        spring_row.group_counts = [int(part) for part in parts[1].split(",")]
        rows.append(spring_row)

    return rows


@functools.cache
def find_num_permutations(spring_row, group_counts):
    # print(f"row: '{spring_row}' how_many={how_many} count={count}")

    if len(group_counts) == 0 and len(spring_row) > 0:
        # we don't have any more matching groups, but we have text left
        # that's ok if they are all ? or .
        if "#" in spring_row:
            return 0
        else:
            return 1

    if len(spring_row) == 0:
        if len(group_counts) == 0:
            return 1
        else:
            return 0

    if spring_row[0] == ".":
        return find_num_permutations(spring_row[1:], group_counts)

    if spring_row[0] == "?":
        return (find_num_permutations("." + spring_row[1:], group_counts) +
                find_num_permutations("#" + spring_row[1:], group_counts))

    if spring_row[0] == "#":
        length = group_counts[0]
        found_match = True
        if len(spring_row) < length:
            return 0
        else:
            if "." in spring_row[0:length]:
                return 0

        # make sure there isn't another # after this match, it must be a ? or a . or the end of line
        if len(spring_row) > length:
            if spring_row[length] == "#":
                return 0

        return find_num_permutations(spring_row[length + 1:], group_counts[1:])


def unfold(spring_row):
    return SpringRow("?".join([spring_row.springs] * 5), spring_row.group_counts * 5)


class SpringRow:

    def __init__(self, springs=None, group_counts=None):
        self.springs = springs
        self.group_counts = group_counts

    def __str__(self):
        return f"{self.springs}: {self.group_counts}"
