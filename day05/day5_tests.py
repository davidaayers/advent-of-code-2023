import day5_funcs
import unittest

test_input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]
almanac = day5_funcs.parse_input(test_input_lines)

class TestDayFive(unittest.TestCase):

    def test_parse_input(self):
        self.assertEqual(almanac.seeds, [79, 14, 55, 13])
        # check some random maps
        self.assertEqual(almanac.mappings["seed-to-soil"].map[99], 51)
        self.assertEqual(almanac.mappings["seed-to-soil"].map[60], 62)
        self.assertEqual(almanac.mappings["humidity-to-location"].map[56], 60)

    def test_find_location_for_seed(self):
        self.assertEqual(day5_funcs.find_location_for_seed(almanac, 79), 82)
        self.assertEqual(day5_funcs.find_location_for_seed(almanac, 14), 43)
        self.assertEqual(day5_funcs.find_location_for_seed(almanac, 55), 86)
        self.assertEqual(day5_funcs.find_location_for_seed(almanac, 13), 35)

    def test_destination_for_and_source_for_are_inverse(self):
        self.assertEqual(day5_funcs.find_location_for_seed(almanac, 79), 82)
        self.assertEqual(day5_funcs.find_seed_for_location(almanac, 82), 79)