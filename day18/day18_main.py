from day18_funcs import *
import utils.util as util
import sys
sys.setrecursionlimit(10000)

input_lines = util.read_file("input.txt")

# Part 1
instructions = parse_input(input_lines)
dig_map = dig_edge(instructions, 1000, 1000, 500, 500)
flood_fill_map(dig_map, 500, 500)
part_1_answer = count_squares(dig_map)
print(f"Part 1: {part_1_answer}")

# Part 2
instructions = parse_input_part2(input_lines)
perimeter = int(count_edge(instructions) / 2 + 1)
vertexes = find_vertexes(instructions)
part_2_answer = calc_area(vertexes) + perimeter
print(f"Part 2: {part_2_answer}")
