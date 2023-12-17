from day15_funcs import *
import unittest

test_input = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]


class TestDayFifteen(unittest.TestCase):

    def test_parsing(self):
        chars = parse_input(test_input_lines)
        self.assertEqual(chars[0], "rn=1")

    def test_calc_hash(self):
        calculated_hash = calc_hash("HASH")
        self.assertEqual(52, calculated_hash)

    def test_calc_hash2(self):
        chars = parse_input(test_input_lines)
        hashes = [calc_hash(char) for char in chars]
        self.assertEqual(1320, sum(hashes))

    def test_calc_hash3(self):
        calculated_hash = calc_hash("rn")
        self.assertEqual(0, calculated_hash)

    def test_perform_initialization(self):
        lens_instructions = parse_input(test_input_lines)
        lens_boxes = perform_initialization(lens_instructions)
        box0 = lens_boxes[0]
        self.assertEqual(2, len(box0.lenses))
        self.assertEqual(["rn", "1"], box0.lenses[0])
        self.assertEqual(["cm", "2"], box0.lenses[1])

        box3 = lens_boxes[3]
        self.assertEqual(3, len(box3.lenses))
        self.assertEqual(["ot", "7"], box3.lenses[0])
        self.assertEqual(["ab", "5"], box3.lenses[1])
        self.assertEqual(["pc", "6"], box3.lenses[2])

    def test_calc_focusing_power(self):
        lens_instructions = parse_input(test_input_lines)
        lens_boxes = perform_initialization(lens_instructions)
        power = calc_focusing_power(lens_boxes)
        self.assertEqual(145, power)
