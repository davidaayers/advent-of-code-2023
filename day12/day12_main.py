import day12_funcs
import utils.util as util

input_lines = util.read_file("input.txt")

springs = day12_funcs.parse_input(input_lines)

part_1_answer = 0
for spring_row in springs:
    answer = day12_funcs.find_num_permutations(spring_row.springs, tuple(spring_row.group_counts))
    part_1_answer += answer

print(f"Part 1: {part_1_answer}")

# https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/

part_2_answer = 0
for spring_row in springs:
    expanded_how_many = []
    expanded_springs = ""
    for i in range(5):
        expanded_springs += spring_row.springs
        expanded_springs += "?"
        expanded_how_many.extend(spring_row.group_counts)

    answer = day12_funcs.find_num_permutations(expanded_springs, tuple(expanded_how_many))
    part_2_answer += answer

# Part 2
print(f"Part 2: {part_2_answer}")