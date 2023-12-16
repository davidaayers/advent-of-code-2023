from day13_funcs import *
import unittest

test_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]

test_input2 = """
.#.##.#.#..#.
....#....#..#
.#..####..##.
..#.#########
....#.....##.
.#####.#..##.
#..#...###..#
###..#.###..#
#.#..#.##....
...#.....####
..#...#......
..#...#.##..#
..#.##..#####
..#.##..#####
..#...#.##..#"""

test_input_lines2 = test_input2.split("\n")
del test_input_lines2[0]

reflections = parse_input(test_input_lines)
reflections2 = parse_input(test_input_lines2)


class TestDayTwelve(unittest.TestCase):

    def test_find_horizontal_reflection(self):
        num_above = find_horizontal_reflection(reflections[1])
        self.assertEqual(num_above[0], 4)

    def test_find_vertical_reflection(self):
        num_left = find_vertical_reflection(reflections[0])
        self.assertEqual(num_left[0], 5)

    def test_calc_answer_for_part_one(self):
        answer = calc_answer_for_part_one(reflections)
        self.assertEqual(405, answer)

    def test_find_smudge(self):
        direction, num = find_reflection_with_smudge(reflections[0])
        self.assertEqual(HORIZONTAL, direction)
        self.assertEqual(3, num)

    def test_find_smudge2(self):
        direction, num = find_reflection_with_smudge(reflections2[0])
        self.assertEqual(VERTICAL, direction)
        self.assertEqual(11, num)

    def test_calc_answer_for_part_two(self):
        answer = calc_answer_for_part_two(reflections)
        self.assertEqual(400, answer)
