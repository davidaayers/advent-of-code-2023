import re


def parse_input(input_lines):
    workflows = {}
    parts = []
    parsing_workflows = True
    for line in input_lines:
        if line == "":
            parsing_workflows = False
            continue

        if parsing_workflows:
            workflow = parse_workflow(line)
            workflows[workflow.name] = workflow
        else:
            matches = re.findall(r"^{\D=(\d+),\D=(\d+),\D=(\d+),\D=(\d+)}$", line)
            part = {
                "x": int(matches[0][0]),
                "m": int(matches[0][1]),
                "a": int(matches[0][2]),
                "s": int(matches[0][3])
            }
            parts.append(part)

    return workflows, parts


def parse_workflow(line):
    matches = re.findall(r"^(\w+){(.+)}$", line)
    name = matches[0][0]
    raw_steps = matches[0][1]

    print(f"workflow={line}")

    steps = []
    for s in raw_steps.split(","):
        matches = re.findall(r"^(\w)(<|>)(\d+):(\w+)$", s)
        if matches:
            var = matches[0][0]
            op = matches[0][1]
            num = int(matches[0][2])
            next_step = matches[0][3]
            steps.append(Step(next_step, var, op, num))
        else:
            steps.append(Step(s))

        print(matches)

    workflow = Workflow(name, steps)
    print(workflow)
    return workflow


def sort_parts(workflows, parts):
    accepted_parts = []
    for part in parts:
        next_workflow_name="in"
        while next_workflow_name != "A" and next_workflow_name != "R":
            print(f"looking for workflow {next_workflow_name}")
            next_workflow_name = workflows[next_workflow_name].execute_workflow(part)

        if next_workflow_name == "A":
            accepted_parts.append(part)

    return accepted_parts


class Workflow:

    def __init__(self, name, steps):
        self.name = name
        self.steps = steps

    def execute_workflow(self, part):
        for step in self.steps:
            if step.op is None:
                return step.next_workflow

            if step.op == ">" and part[step.var] > step.num:
                return step.next_workflow

            if step.op == "<" and part[step.var] < step.num:
                return step.next_workflow

    def __str__(self):
        workflow_str = self.name + ":\n"
        for step in self.steps:
            workflow_str += f"   {step}\n"
        return workflow_str


class Step:

    def __init__(self, next_workflow, var=None, op=None, num=None):
        self.next_workflow = next_workflow
        self.num = num
        self.var = var
        self.op = op

    def execute_step(self, part):
        # execute and return next step
        pass

    def __str__(self):
        if self.op is None:
            return self.next_workflow
        return f"{self.var}{self.op}{self.num}: {self.next_workflow}"

    def __repr__(self):
        return self.__str__()
