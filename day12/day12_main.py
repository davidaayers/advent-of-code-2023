import day12_funcs
import utils.util as util

input_lines = util.read_file("input.txt")

springs = day12_funcs.parse_input(input_lines)

part_1_answer = 0
for spring_row in springs:
    answer = day12_funcs.find_num_permutations(spring_row.springs, spring_row.how_many, 0, 0)
    part_1_answer += answer

print(f"Part 1: {part_1_answer}")

# Part 2
part_2_answer = 0
print(f"Part 2: {part_2_answer}")