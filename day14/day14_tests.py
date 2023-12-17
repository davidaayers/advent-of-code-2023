from day14_funcs import *
import unittest

test_input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

test_input_lines = test_input.split("\n")
del test_input_lines[0]


class TestDayFourteen(unittest.TestCase):

    def test_parsing(self):
        platform = parse_input(test_input_lines)
        self.assertEqual(platform.platform_map[0][0], "O")
        self.assertEqual(platform.platform_map[0][1], ".")

    def test_tilt(self):
        platform = parse_input(test_input_lines)
        platform.tilt(NORTH)
        self.assertEqual("OOOO.#.O..", "".join(platform.platform_map[0]))
        self.assertEqual("OO..#....#", "".join(platform.platform_map[1]))
        print(map_array_to_str(platform.platform_map))

    def test_calc_load_in_dir(self):
        platform = parse_input(test_input_lines)
        platform.tilt(NORTH)
        total_load = calc_load_on_north_pillar(platform)
        self.assertEqual(136, total_load)

    def test_calc_load_after_1_cycle(self):
        platform = parse_input(test_input_lines)
        load = calc_load_after_cycles(platform, 1)
        after = """.....#....\n....#...O#\n...OO##...\n.OO#......\n.....OOO#.\n.O#...O#.#\n....O#....\n......OOOO\n#...O###..\n#..OO#....\n"""
        self.assertEqual(after, map_array_to_str(platform.platform_map))

    def test_calc_load_after_2_cycles(self):
        platform = parse_input(test_input_lines)
        load = calc_load_after_cycles(platform, 2)
        after = """.....#....\n....#...O#\n.....##...\n..O#......\n.....OOO#.\n.O#...O#.#\n....O#...O\n.......OOO\n#..OO###..\n#.OOO#...O\n"""
        platform_actual = map_array_to_str(platform.platform_map)
        self.assertEqual(after, platform_actual)

    def test_calc_load_after_3_cycles(self):
        platform = parse_input(test_input_lines)
        load = calc_load_after_cycles(platform, 3)
        after = """.....#....\n....#...O#\n.....##...\n..O#......\n.....OOO#.\n.O#...O#.#\n....O#...O\n.......OOO\n#...O###.O\n#.OOO#...O\n"""
        platform_actual = map_array_to_str(platform.platform_map)
        self.assertEqual(after, platform_actual)


