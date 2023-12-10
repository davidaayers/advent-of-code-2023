import day10_funcs
import utils.util as util

input = util.read_file("input.txt")

pipe_map = day10_funcs.parse_input(input)
print(pipe_map)
part_1_answer = len(pipe_map.loop_nodes)/2
print(f"Part 1: {part_1_answer}")

# Part 2
part_2_answer = 0
print(f"Part 2: {part_2_answer}")