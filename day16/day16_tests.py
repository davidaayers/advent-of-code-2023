from day16_funcs import *
import unittest

test_input = """
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""

test_input_lines = test_input.split("\n")
del test_input_lines[0]

test_input2 = r"""
\...\.............
.............|/...
....\......-.....|
|.....-....\.|....
............../.|.
.-.-...|....-.-...
..........\.....|.
...../............
......\......\....
.....|./..........
...../...../......
..\...............
....|.........-.|.
.........-........
.............|....
................./"""

test_input_lines2 = test_input2.split("\n")
del test_input_lines2[0]


class TestDaySixteen(unittest.TestCase):

    def test_parsing(self):
        contraption_map = parse_input(test_input_lines)
        self.assertEqual(".", contraption_map.puzzle_map.map_squares[0][0])
        print(contraption_map.puzzle_map)

    def test_project_beam(self):
        contraption_map = parse_input(test_input_lines)
        print(contraption_map.puzzle_map)
        project_beam(contraption_map)
        print(contraption_map.light_map)
        self.assertEqual(46, count_illuminated_squares(contraption_map))

    def test_project_beam2(self):
        contraption_map = parse_input(test_input_lines2)
        print(contraption_map.puzzle_map)
        project_beam(contraption_map)
        print(contraption_map.light_map)
        self.assertEqual(46, count_illuminated_squares(contraption_map))
