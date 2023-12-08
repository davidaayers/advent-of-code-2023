import re


def parse_input(lines_original):
    lines = lines_original.copy()
    directions = lines[0]
    del lines[0]
    del lines[0]
    desert_map = dict()
    # first go through and create all the nodes
    for line in lines:
        parts = re.search(r"^(\w{3}).*\((\w{3}).*(\w{3})\)$", line)
        node_name = parts.group(1)
        node = Node(node_name, parts.group(2), parts.group(3))
        desert_map[node_name] = node

    # now, connect the nodes
    for node in desert_map.values():
        left = desert_map[node.left_str]
        right = desert_map[node.right_str]
        node.set_adjacent(left, right)

    return [directions, desert_map]


def walk_map(desert_map):
    directions = desert_map[0]
    nodes = desert_map[1]

    # start with "AAA"
    current_node = nodes["AAA"]

    steps = 0
    while current_node.name != "ZZZ":
        for d in directions:
            steps += 1
            current_node = current_node.adjacent[d]

    return steps


class Node:

    def __init__(self, name, left_str, right_str):
        self.name = name
        self.left_str = left_str
        self.right_str = right_str
        self.adjacent = dict()

    def set_adjacent(self, left, right):
        self.adjacent["L"] = left
        self.adjacent["R"] = right

    def __str__(self):
        return f"Name = {self.name}"

    def __repr__(self):
        return self.__str__()