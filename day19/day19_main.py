from day19_funcs import *
import utils.util as util


def main():
    input_lines = util.read_file("input.txt")

    # Part 1
    workflows, parts = parse_input(input_lines)
    sorted_parts = sort_parts(workflows, parts)
    part_1_answer = 0
    for part in sorted_parts:
        part_1_answer += sum(part.values())

    print(f"Part 1: {part_1_answer}")

    # Part 2
    part_2_answer = 0
    print(f"Part 2: {part_2_answer}")


if __name__ == "__main__":
    main()
