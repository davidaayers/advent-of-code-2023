import re

from utils.util import *

instr_to_dir = {
    "U": NORTH,
    "D": SOUTH,
    "R": EAST,
    "L": WEST
}


def parse_input(input_lines):
    instructions = []
    for instruction in input_lines:
        matches = re.findall(r"^(\w) (\d+) \(#(\w{6})\)$", instruction, )
        instr = matches[0][0]
        meters = int(matches[0][1])
        color = matches[0][2]
        instructions.append((instr_to_dir[instr], meters, color))
    return instructions


def dig_edge(instructions, width, height, x, y):
    dig_map = PuzzleMap(width, height)
    dig_map.add_symbol(x, y, "#")
    for instruction in instructions:
        for r in range(instruction[1]):
            x += CARDINAL_DIRECTIONS[instruction[0]][1]
            y += CARDINAL_DIRECTIONS[instruction[0]][0]
            dig_map.add_symbol(x, y, "#")

    return dig_map


# Flood fill from https://lvngd.com/blog/flood-fill-algorithm-python/
def flood_fill_map(dig_map, x, y):
    # move the start of the flood to the interior of the polygon
    x += 1
    y += 1
    width = dig_map.width
    height = dig_map.height

    def fill(x, y, start_symbol, end_symbol):
        # if the square is not the same color as the starting point
        if dig_map.map_squares[y][x] != start_symbol:
            return
        # if the square is not the new color
        elif dig_map.map_squares == end_symbol:
            return
        else:
            # update the color of the current square to the replacement color
            dig_map.map_squares[y][x] = end_symbol
            neighbors = [(x - 1, y), (x + 1, y), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1),
                         (x, y - 1), (x, y + 1)]
            for n in neighbors:
                if 0 <= n[0] <= width - 1 and 0 <= n[1] <= height - 1:
                    fill(n[0], n[1], start_symbol, end_symbol)

    fill(x, y, ".", "#")


def count_squares(dig_map):
    cnt = 0
    for y in range(dig_map.height):
        for x in range(dig_map.width):
            if dig_map.map_squares[y][x] == "#":
                cnt += 1
    return cnt
