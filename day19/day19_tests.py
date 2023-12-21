from day19_funcs import *
import unittest

test_input = r"""
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]


class TestDayNineteen(unittest.TestCase):

    def test_parsing(self):
        workflows, parts = parse_input(test_input_lines)
        self.assertEqual("px", workflows["px"].name)
        self.assertEqual("lnx", workflows["lnx"].name)

    def test_sort_parts(self):
        workflows, parts = parse_input(test_input_lines)
        sorted_parts = sort_parts(workflows, parts)
        answer = 0
        for part in sorted_parts:
            answer += sum(part.values())
        self.assertEqual(19114, answer)