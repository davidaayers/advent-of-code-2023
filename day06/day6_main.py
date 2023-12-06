from functools import reduce

import day6_funcs
import utils.util as util
import operator

input = util.read_file("input.txt")

races = day6_funcs.parse_input(input)
winners = [day6_funcs.find_num_ways_to_win(race) for race in races]
product_of_winners = reduce(operator.mul, winners)

part_1_answer = product_of_winners
print(f"Part 1: {part_1_answer}")

race2 = [46857582, 208141212571410]
winners2 = day6_funcs.find_num_ways_to_win(race2)

# Part 2
part_2_answer = winners2
print(f"Part 2: {part_2_answer}")