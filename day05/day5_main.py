import sys

import day5_funcs
import utils.util as util

input = util.read_file("input.txt")

almanac = day5_funcs.parse_input(input)
seed_locations = []
for seed in almanac.seeds:
    location = day5_funcs.find_location_for_seed(almanac, seed)
    seed_locations.append(location)

seed_locations.sort()
part_1_answer = seed_locations[0]
print(f"Part 1: {part_1_answer}")
