import re


def parse_input(input_lines):
    seeds = [int(n) for n in input_lines[0].split(":")[1].split()]
    almanac = Almanac(seeds)
    almanac.add_map("seed-to-soil", create_map(input_lines, "seed-to-soil"))
    almanac.add_map("soil-to-fertilizer", create_map(input_lines, "soil-to-fertilizer"))
    almanac.add_map("fertilizer-to-water", create_map(input_lines, "fertilizer-to-water"))
    almanac.add_map("water-to-light", create_map(input_lines, "water-to-light"))
    almanac.add_map("light-to-temperature", create_map(input_lines, "light-to-temperature"))
    almanac.add_map("temperature-to-humidity", create_map(input_lines, "temperature-to-humidity"))
    almanac.add_map("humidity-to-location", create_map(input_lines, "humidity-to-location"))

    return almanac


def find_map(input_lines, map_name):
    map_start, map_end = 0, 0
    found_start = False
    found_end = False
    for idx, line in enumerate(input_lines):
        if line.startswith(map_name):
            map_start = idx + 1
            found_start = True

        # we're looking for the next line that *doesn't* start with a number, that's the end
        elif found_start and re.match("^\D", line):
            map_end = idx - 1
            found_end = True
            break

    # Handle the edge case -- we got to the end of the list and didn't find the end,
    # which means we're on the last map
    if not found_end:
        map_end = len(input_lines)

    return input_lines[map_start:map_end]


def create_map(input_lines, map_name):
    map_data = find_map(input_lines, map_name)
    almanac_map = AlmanacMap(map_name)
    for data_line in map_data:
        data = [int(n) for n in data_line.split()]
        almanac_map.add_mappings(data[0], data[1], data[2])

    return almanac_map


def find_location_for_seed(almanac, seed):
    map_order = [
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location"
    ]

    current_location = almanac.mappings["seed-to-soil"].destination_for(seed)
    for almanac_map in map_order:
        current_location = almanac.mappings[almanac_map].destination_for(current_location)

    return current_location


def find_seed_for_location(almanac, seed):
    map_order = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
    ]

    map_order.reverse()

    current_location = almanac.mappings["humidity-to-location"].source_for(seed)
    for almanac_map in map_order:
        current_location = almanac.mappings[almanac_map].source_for(current_location)

    return current_location


class AlmanacMap:

    def __init__(self, map_name):
        self.map_name = map_name
        self.mappings = []

    def add_mappings(self, destination, source, length):
        self.mappings.append([destination, source, length])

    def destination_for(self, source):
        for mapping in self.mappings:
            if mapping[1] <= source <= mapping[1] + mapping[2]:
                diff = mapping[0] - mapping[1]
                destination = source + diff
                return destination

        return source

    def source_for(self, destination):
        for mapping in self.mappings:
            if mapping[0] <= destination <= mapping[0] + mapping[2]:
                diff = mapping[1] - mapping[0]
                source = destination + diff
                return source

        return destination

    def __str__(self):
        return f"{self.map_name}: {self.map}"


class Almanac:

    def __init__(self, seeds):
        self.seeds = seeds
        self.mappings = dict()

    def add_map(self, name, almanac_map):
        self.mappings[name] = almanac_map
