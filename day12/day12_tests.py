import day12_funcs
import unittest

test_input = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
#.#?. 1,1"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]


class TestDayTwelve(unittest.TestCase):

    def test_parsing(self):
        springs = day12_funcs.parse_input(test_input_lines)

    def test_find_num_permutations(self):
        springs = day12_funcs.parse_input(test_input_lines)
        answers = [1, 4, 1, 1, 4, 10, 1]

        for idx, spring_row in enumerate(springs):
            # print(f"Checking: {spring_row} with expected answer of {answers[idx]}")
            answer = day12_funcs.find_num_permutations(spring_row.springs, tuple(spring_row.group_counts))
            # print(f"{spring_row} -> {answer}")
            self.assertEqual(answers[idx], answer)

