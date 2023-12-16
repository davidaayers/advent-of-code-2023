from day13_funcs import *
import utils.util as util

input_lines = util.read_file("input.txt")

# Part 1
reflections = parse_input(input_lines)
part_1_answer = calc_answer_for_part_one(reflections)
print(f"Part 1: {part_1_answer}")

# Part 2
part_2_answer = 0
print(f"Part 2: {part_2_answer}")