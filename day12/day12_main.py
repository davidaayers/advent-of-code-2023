import day12_funcs
import utils.util as util

input_lines = util.read_file("input.txt")

springs = day12_funcs.parse_input(input_lines)

part_1_answer = 0
for spring_row in springs:
    answer = day12_funcs.find_num_permutations(spring_row.springs, tuple(spring_row.how_many), 0)
    part_1_answer += answer

print(f"Part 1: {part_1_answer}")

part_2_answer = 0
for spring_row in springs:
    expanded_how_many = []
    expanded_springs = ""
    for i in range(5):
        expanded_springs += spring_row.springs
        expanded_springs += "?"
        expanded_how_many.extend(spring_row.how_many)

    t = tuple(expanded_how_many)
    answer = day12_funcs.find_num_permutations(expanded_springs, t, 0)
    part_2_answer += answer

# Part 2
part_2_answer = 0
print(f"Part 2: {part_2_answer}")