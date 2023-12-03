import day3_funcs
import unittest

test_schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

test_schematic2 = """
12.......*..
+.........34
.......-12..
..78........
..*....60...
78..........
.......23...
....90*12...
............
2.2......12.
.*.........*
1.1.......56"""


class TestDayThree(unittest.TestCase):

    def test_parse_schematic(self):
        schematic_lines = test_schematic.split("\n")
        del schematic_lines[0]
        schematic = day3_funcs.parse_schematic(schematic_lines)
        # Check a few random parts of the schematic to make sure it parsed correctly
        self.assertEqual(schematic[0][0], "4")
        self.assertEqual(schematic[9][9], ".")
        self.assertEqual(schematic[4][0], "6")
        self.assertEqual(schematic[7][9], ".")

    def test_find_part_numbers_1(self):
        schematic_lines = test_schematic.split("\n")
        del schematic_lines[0]
        schematic = day3_funcs.parse_schematic(schematic_lines)
        part_numbers = day3_funcs.extract_symbols(schematic)

        self.assertEqual(sum(part_numbers), 4361)

    def test_find_part_numbers_2(self):
        schematic_lines = test_schematic2.split("\n")
        del schematic_lines[0]
        schematic = day3_funcs.parse_schematic(schematic_lines)
        part_numbers = day3_funcs.extract_symbols(schematic)

        self.assertEqual(sum(part_numbers), 413)
