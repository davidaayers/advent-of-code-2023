import utils.util
from utils.pathfinding import *


def parse_input(input_lines):
    width = len(input_lines[0])
    height = len(input_lines)
    island_map = IslandMap(width, height)

    for y,line in enumerate(input_lines):
        for x, weight in enumerate(line):
            island_map.weights[(x,y)] = float(weight)
            island_map.map_squares[y][x] = weight

    return island_map


class IslandMap(GridWithWeights):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.map_squares = [["." for x in range(width)] for y in range(height)]

    def __str__(self):
        return utils.util.map_array_to_str(self.map_squares)


def find_path(island_map: IslandMap):
    start = (0,0)
    end = (island_map.width-1, island_map.height-1)

    came_from, cost_so_far = a_star_search_new(island_map, start, end)
    path = reconstruct_path(came_from, start, end)
    print(path)



def a_star_search_new(graph: WeightedGraph, start: Location, goal: Location):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: dict[Location, Optional[Location]] = {}
    cost_so_far: dict[Location, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current: Location = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far