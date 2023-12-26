import re
from solutions import Solution

class Day09(Solution):
    def __init__(self):
        super().__init__(day=9, year=2023)

    def parse_input(self):
        self.lines = [
            [int(x) for x in re.findall(r'-?\d+', line)]
            for line in self.inp
        ]

    def create_history(self, line):
        history = [line]
        cur_line = line
        # 1. Create history
        while not all([x == 0 for x in cur_line]):
            next_line = [cur_line[i+1] - cur_line[i]
                         for i in range(len(cur_line)-1)]
            history.append(next_line)
            cur_line = next_line
        return history

    def predict_forward(self, line):
        history = self.create_history(line)
        history[-1].append(0)
        for i in range(len(history)-2, -1, -1):
            history[i].append(history[i][-1] + history[i+1][-1])
        return history[0][-1]

    def predict_backward(self, line):
        history = self.create_history(line)
        history[-1] = [0] + history[-1]
        for i in range(len(history)-2, -1, -1):
            history[i] = [history[i][0] - history[i+1][0]] + history[i]
        return history[0][0]

    def problem_1(self) -> int:
        solution = 0
        for line in self.lines:
            pred = self.predict_forward(line)
            solution += pred
        return solution

    def problem_2(self) -> int:
        solution = 0
        for line in self.lines:
            pred = self.predict_backward(line)
            solution += pred
        return solution

if __name__ == '__main__':
    print(Day09())