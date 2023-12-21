import re

from utils.util import *

instr_to_dir = {
    "U": NORTH,
    "D": SOUTH,
    "R": EAST,
    "L": WEST
}

num_to_dir = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U"
}

def parse_input(input_lines):
    instructions = []
    for instruction in input_lines:
        matches = re.findall(r"^(\w) (\d+) \(#(\w{6})\)$", instruction )
        instr = matches[0][0]
        meters = int(matches[0][1])
        color = matches[0][2]
        instructions.append((instr_to_dir[instr], meters, color))
    return instructions


def parse_input_part2(input_lines):
    instructions = []
    for instruction in input_lines:
        matches = re.findall(r"^.+\(#(\w{5})(\d{1})\)$", instruction )
        meters = int(matches[0][0], 16)
        instr = matches[0][1]
        instructions.append((instr_to_dir[num_to_dir[instr]],meters,0))
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


def count_edge(instructions):
    cnt = 1
    for instruction in instructions:
        for r in range(instruction[1]):
            cnt += 1

    return cnt



def find_vertexes(instructions):
    vertexes = []
    last_vertex = (0, 0)
    vertexes.append(last_vertex)
    for instruction in instructions:
        x, y = 0, 0
        for r in range(instruction[1]):
            x += CARDINAL_DIRECTIONS[instruction[0]][1]
            y += CARDINAL_DIRECTIONS[instruction[0]][0]

        last_vertex = (last_vertex[0] + x, last_vertex[1] + y)
        vertexes.append(last_vertex)

    return vertexes


def calc_area(vertexes):
    n = len(vertexes)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertexes[i][0] * vertexes[j][1]
        area -= vertexes[j][0] * vertexes[i][1]
    area = abs(area) / 2.0
    return area


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
