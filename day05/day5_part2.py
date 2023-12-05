import day5_funcs
import utils.util as util

input = util.read_file("input.txt")

almanac = day5_funcs.parse_input(input)

ranges = []
for seed_idx in range(0, len(almanac.seeds), 2):
    seed_location, seed_range = almanac.seeds[seed_idx], almanac.seeds[seed_idx+1]
    ranges.append([seed_location, seed_location+seed_range])

print(ranges)

location = 0

should_continue = True
while should_continue:
    seed_for_location = day5_funcs.find_seed_for_location(almanac, location)

    for r in ranges:
        if r[0] <= seed_for_location <= r[1]:
            print(f"Solution is {location}")
            should_continue = False
            break

    location += 1

    if location % 1000000 == 0:
        print(f"Location cnt at {location}")


