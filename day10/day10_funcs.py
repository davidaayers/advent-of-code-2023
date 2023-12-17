from utils.util import *


def parse_input(input_lines):
    width = len(input_lines[0])
    height = len(input_lines)
    pipe_map = PipeMap(width, height)

    full_map = [["." for x in range(width)] for y in range(height)]
    for y in range(height):
        for x, map_symbol in enumerate(input_lines[y]):
            full_map[y][x] = map_symbol
            if map_symbol == "S":
                pipe_map.start_x = x
                pipe_map.start_y = y

    nodes = []
    visited_nodes = []
    start_node = MapNode(pipe_map.start_x, pipe_map.start_y, "S")
    pipe_map.start_node = start_node
    nodes.append(start_node)
    pipe_map.add_loop_node(start_node)

    while len(nodes) > 0:
        next_node = nodes.pop(0)
        visited_nodes.append(next_node)
        adjacent_nodes = []
        for direction in DIRS:
            if next_node.can_connect_in_direction(direction, full_map):
                # found a valid node
                test_x = next_node.x + CARDINAL_DIRECTIONS[direction][1]
                test_y = next_node.y + CARDINAL_DIRECTIONS[direction][0]
                test_square = full_map[test_y][test_x]

                node = MapNode(test_x, test_y, test_square)
                adjacent_nodes.append(node)
                if node not in visited_nodes:
                    nodes.append(node)
                    if node not in pipe_map.loop_nodes:
                        pipe_map.add_loop_node(node)

        next_node.adjacent_nodes.extend(adjacent_nodes)

    return pipe_map


def find_farthest_num_steps(pipe_map):
    start_node = pipe_map.start_node
    next_steps = [start_node.adjacent_nodes[0], start_node.adjacent_nodes[1]]
    prev_steps = [start_node, start_node]

    steps = 1

    while True:
        steps += 1
        # find the next step in each path
        for idx in range(2):
            step = next_steps[idx]
            prev_step = prev_steps[idx]

            n = step.adjacent_nodes[0] if step.adjacent_nodes[1] == prev_step else step.adjacent_nodes[1]
            # these nodes aren't connected, so fetch it from the map
            next_step = [node for node in pipe_map.loop_nodes if node == n][0]
            next_steps[idx] = next_step
            prev_steps[idx] = step

        if steps % 100 == 0:
            print(f"Steps = {steps}")

        # if we ended up back at the start, bail
        if next_steps[0].map_symbol == "S" or next_steps[1].map_symbol == "S":
            print("Back at the start, bailing")
            break

        # if both next steps have arrived at the same spot, we found the
        # furthest point
        if next_steps[0] == next_steps[1]:
            break

    return steps


def count_inside(pipe_map):
    num_inside = 0
    inside = False
    last_corner = None
    for y in range(pipe_map.height):
        for x in range(pipe_map.width):
            check_char = pipe_map.pipe_map[y][x]
            if check_char == "." and inside:
                num_inside += 1

            if check_char == "|":
                inside = not inside

            if check_char == "L" or check_char == "F":
                last_corner = check_char

            if check_char == "J":
                if last_corner == "F":
                    inside = not inside
                last_corner = check_char

            if check_char == "7":
                if last_corner == "L":
                    inside = not inside
                last_corner = check_char

    return num_inside

class PipeMap:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.start_node = None
        self.pipe_map = [["." for x in range(width)] for y in range(height)]
        self.loop_nodes = []

    def __str__(self):
        return map_array_to_str(self.pipe_map)

    def add_map_symbol(self, x, y, map_symbol):
        self.pipe_map[y][x] = map_symbol

    def add_loop_node(self, node):
        self.loop_nodes.append(node)
        self.add_map_symbol(node.x, node.y, node.map_symbol)


class MapNode:

    def __init__(self, x, y, map_symbol):
        self.x = x
        self.y = y
        self.map_symbol = map_symbol
        self.adjacent_nodes = []

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"[{self.x}, {self.y}]: {self.map_symbol}"

    def __repr__(self):
        return self.__str__()

    def can_connect_in_direction(self, direction, map_array):
        test_dir = CARDINAL_DIRECTIONS[direction]
        test_x = self.x + test_dir[1]
        test_y = self.y + test_dir[0]
        if test_x >= len(map_array[0]) or test_x < 0 or test_y >= len(map_array) or test_y < 0:
            return False

        test_symbol = map_array[test_y][test_x]

        # back at the start?
        if test_symbol == "S":
            return True

        if direction == NORTH:
            return self.map_symbol in ["S", "|", "L", "J"] and test_symbol in ["S", "|", "7", "F"]

        if direction == SOUTH:
            return self.map_symbol in ["S", "|", "7", "F"] and test_symbol in ["S", "|", "L", "J"]

        if direction == EAST:
            return self.map_symbol in ["S", "-", "L", "F"] and test_symbol in ["S", "-", "7", "J"]

        if direction == WEST:
            return self.map_symbol in ["S", "-", "7", "J"] and test_symbol in ["S", "-", "L", "F"]

        return False
