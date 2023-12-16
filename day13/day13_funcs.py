def parse_input(input_lines):
    reflections = []
    this_reflection = []
    for line in input_lines:
        if line == "":
            reflections.append(this_reflection.copy())
            this_reflection = []
        else:
            this_reflection.append(line)

    # the last one
    reflections.append(this_reflection.copy())
    return reflections


def find_vertical_reflection(reflection):
    # rotate 90 degrees, then use find_horizontal_reflection
    rotated_reflection = []

    for x in range(len(reflection[0])):
        line = ""
        for y in range(len(reflection) - 1, -1, -1):
            line += reflection[y][x]
        rotated_reflection.append(line)

    return find_horizontal_reflection(rotated_reflection)


def find_horizontal_reflection(reflection):
    # find two rows in a row that are the same
    for idx, line in enumerate(reflection):
        if idx < len(reflection) - 1:
            next_line = reflection[idx + 1]
            # Did we find a possible reflection?
            if line == next_line:
                # This assumes there is only *one* actual reflection, so if
                # we've found it, we can bail out
                if is_actual_reflection(reflection, idx, idx + 1):
                    return True, idx + 1

    return False, None


def is_actual_reflection(reflection, l1, l2):
    check = 1
    reflection_reaches_edge = True
    while True:
        c1 = l1 - check
        c2 = l2 + check

        # Did we reach the edge?
        if c1 < 0 or c2 == len(reflection):
            break

        # Do the reflected lines match?
        if reflection[c1] != reflection[c2]:
            reflection_reaches_edge = False
            break

        check += 1

    if reflection_reaches_edge:
        return True
    else:
        return False


def calc_answer_for_part_one(reflections):
    answer = 0
    for idx, reflection in enumerate(reflections):
        is_horizontal_reflection, num_horizontal = find_horizontal_reflection(reflection)
        is_vertical_reflection, num_vertical = find_vertical_reflection(reflection)

        if is_horizontal_reflection:
            answer = answer + num_horizontal * 100
        else:
            answer = answer + num_vertical

    return answer
