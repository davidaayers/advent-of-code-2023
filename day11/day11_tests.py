import day11_funcs
import unittest

test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

test_input_lines = test_input.split("\n")
del test_input_lines[0]

post_expansion = """
....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""
post_expansion_input_lines = post_expansion.split("\n")
del post_expansion_input_lines[0]

galaxy_map = day11_funcs.parse_input(test_input_lines)


class TestDayEleven(unittest.TestCase):

    def test_parsing(self):
        for y in range(len(post_expansion_input_lines)):
            for x in range(len(post_expansion_input_lines[0])):
                map_char = post_expansion_input_lines[y][x]
                self.assertEqual(map_char, galaxy_map.map_symbols[y][x])

    def test_translation(self):
        old = []
        new = []
        for galaxy in galaxy_map.galaxies:
            old_x = galaxy.x
            old_y = galaxy.y
            old.append([old_x, old_y])
            new_x, new_y = galaxy_map.translate(old_x, old_y, 1)
            new.append([new_x, new_y])

        # check a few
        self.assertEqual(new[0][0], 4)
        self.assertEqual(new[0][1], 0)
        self.assertEqual(new[1][0], 9)
        self.assertEqual(new[1][1], 1)

    def test_calc_distances(self):
        total = day11_funcs.calc_distances(galaxy_map, 1)
        self.assertEqual(total, 374)
