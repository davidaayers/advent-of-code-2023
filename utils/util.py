NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

DIRS = [NORTH, WEST, SOUTH, EAST]

CARDINAL_DIRECTIONS = {
    NORTH: [-1, 0],
    SOUTH: [1, 0],
    EAST: [0, 1],
    WEST: [0, -1]
}

DIRECTION_NAMES = {
    NORTH: "North",
    SOUTH: "South",
    EAST: "East",
    WEST: "West"
}


def read_file(file_name):
    with open(file_name) as f:
        content = f.read().splitlines()
    return content


def map_array_to_str(map_array, use_box_chars=False):
    box_chars = {
        "|": "\u2502",
        "-": "\u2500",
        "L": "\u2514",
        "J": "\u2518",
        "7": "\u2510",
        "F": "\u250C"
    }
    ascii_map = ""
    for map_line in map_array:
        ascii_map += ("".join(map_line))
        if use_box_chars:
            for char in box_chars:
                ascii_map = ascii_map.replace(char, box_chars[char])
        ascii_map += "\n"
    return ascii_map


def parse_puzzle_map(input_lines):
    width = len(input_lines[0])
    height = len(input_lines)
    puzzle_map = PuzzleMap(width, height)

    for y, line in enumerate(input_lines):
        for x, symbol in enumerate(line):
            puzzle_map.add_symbol(x, y, symbol)

    return puzzle_map


class PuzzleMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_squares = [["." for x in range(width)] for y in range(height)]

    def add_symbol(self, x, y, symbol):
        self.map_squares[y][x] = symbol

    def is_in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def __str__(self):
        return map_array_to_str(self.map_squares)

    def __repr__(self):
        return map_array_to_str(self.map_squares)

    def __copy__(self):
        other = PuzzleMap(self.width, self.height)
        other.map_squares = self.map_squares.copy()
        return other
