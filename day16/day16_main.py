from day16_funcs import *
import utils.util as util

input_lines = util.read_file("input.txt")

contraption_map = parse_input(input_lines)
project_beam(contraption_map, Beam(EAST, -1, 0))

# Part 1
part_1_answer = count_illuminated_squares(contraption_map)
print(f"Part 1: {part_1_answer}")

# Part 2
contraption_map = parse_input(input_lines)
part_2_answer = find_best_beam(contraption_map)
print(f"Part 2: {part_2_answer}")
