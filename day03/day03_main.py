import day3_funcs
import utils.util as util

input = util.read_file("input.txt")

schematic = day3_funcs.parse_schematic(input)
part_numbers = day3_funcs.find_part_numbers(schematic)

part_1_answer = sum(part_numbers)
print(f"Part 1: {part_1_answer}")

# Part 2
symbols = day3_funcs.extract_symbols(schematic)
gears = [symbol for symbol in symbols if symbol.is_gear()]
part_2_answer = sum(gear.gear_ratio() for gear in gears)
print(f"Part 2: {part_2_answer}")