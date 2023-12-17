from day15_funcs import *
import utils.util as util

input_lines = util.read_file("input.txt")

# Part 1
chars = parse_input(input_lines)
hashes = [calc_hash(char) for char in chars]

part_1_answer = sum(hashes)
print(f"Part 1: {part_1_answer}")

# Part 2
lens_instructions = parse_input(input_lines)
lens_boxes = perform_initialization(lens_instructions)
part_2_answer = calc_focusing_power(lens_boxes)

print(f"Part 2: {part_2_answer}")
