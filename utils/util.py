NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

DIRS = [NORTH, EAST, SOUTH, WEST]

CARDINAL_DIRECTIONS = {
    NORTH: [-1, 0],
    SOUTH: [1, 0],
    EAST: [0, 1],
    WEST: [0, -1]
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
