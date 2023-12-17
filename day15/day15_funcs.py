import re


def parse_input(input_lines):
    return input_lines[0].split(",")


def calc_hash(chars):
    calculated_hash = 0
    for c in chars:
        calculated_hash += ord(c)
        calculated_hash *= 17
        calculated_hash = calculated_hash % 256

    return calculated_hash


def perform_initialization(lens_instructions):
    lens_boxes = dict()
    for i in range(256):
        lens_boxes[i] = LensBox(i)

    for instruction in lens_instructions:
        matches = re.findall(r"^(\w+)([-=])(\d?)$", instruction, re.MULTILINE)
        instr = matches[0][0]
        operation = matches[0][1]
        lens_strength = matches[0][2]

        lens = [instr, lens_strength]
        box_num = calc_hash(instr)

        # grab the box
        lens_box = lens_boxes[box_num]

        if operation == "=":
            # Does this lens already exist? Replace it
            processed = False
            for box_lens in lens_box.lenses:
                if box_lens[0] == instr:
                    box_lens[1] = lens_strength
                    processed = True
                    break

            if not processed:
                lens_box.lenses.append(lens)

        if operation == "-":
            # See if it's there
            indexes = [idx for (idx, item) in enumerate(lens_box.lenses) if item[0] == instr]
            if indexes:
                lens_box.lenses.pop(indexes[0])

    return lens_boxes


def calc_focusing_power(lens_boxes):
    total_lens_power = 0

    for box_idx in range(256):
        lens_box = lens_boxes[box_idx]
        box_no = lens_box.box_no

        for lens_idx, lens in enumerate(lens_box.lenses):
            # lens is a list ['rn','1']
            lens_power = ((box_no + 1) * (lens_idx + 1)) * int(lens[1])
            total_lens_power += lens_power

    return total_lens_power


class LensBox:

    def __init__(self, box_no):
        self.box_no = box_no
        self.lenses = []

    def __str__(self):
        return f"{self.box_no}: {self.lenses}"
