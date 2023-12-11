def parse_input(input_lines):
    width = len(input_lines[0])
    height = len(input_lines)
    orig_map = []
    rows_to_expand = []
    galaxies = []
    for y in range(height):
        orig_map.append([])
        num_dots = 0
        for x in range(width):
            map_char = input_lines[y][x]
            orig_map[y].append(map_char)
            if map_char == ".":
                num_dots += 1
            if map_char == "#":
                galaxies.append(Galaxy(x, y))
        if num_dots == width:
            rows_to_expand.append(y)

    columns_to_expand = []
    for x in range(width):
        num_dots = 0
        for y in range(height):
            map_char = orig_map[y][x]
            if map_char == ".":
                num_dots += 1

        if num_dots == height:
            columns_to_expand.append(x)

    galaxy_map = GalaxyMap(height, width)
    galaxy_map.map_symbols = orig_map
    galaxy_map.galaxies = galaxies
    galaxy_map.rows_to_expand = rows_to_expand
    galaxy_map.columns_to_expand = columns_to_expand

    return galaxy_map


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def calc_distances(galaxy_map, factor):
    total_distance = 0
    for idx in range(len(galaxy_map.galaxies)):
        # compare to all others
        for idx2 in range(idx + 1, len(galaxy_map.galaxies)):
            gal1 = galaxy_map.galaxies[idx]
            gal2 = galaxy_map.galaxies[idx2]
            x1, y1 = galaxy_map.translate(gal1.x, gal1.y, factor)
            x2, y2 = galaxy_map.translate(gal2.x, gal2.y, factor)
            distance = manhattan_distance(x1, y1, x2, y2)
            total_distance += distance
    return total_distance


class GalaxyMap:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map_symbols = None
        self.galaxies = None
        self.rows_to_expand = None
        self.columns_to_expand = None

    def translate(self, x, y, factor):
        x_to_add = 0
        for r in self.columns_to_expand:
            if r < x:
                x_to_add += factor

        y_to_add = 0
        for c in self.rows_to_expand:
            if c < y:
                y_to_add += factor

        return x + x_to_add, y + y_to_add


class Galaxy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
