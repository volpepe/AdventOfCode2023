import re
from solutions import Solution

class Day01(Solution):
    def __init__(self):
        super().__init__(day=1, year=2023)

    def problem_1(self) -> int:
        glob_sum = 0
        for line in self.inp:
            matches = re.findall(r'\d', line)
            glob_sum += (int(matches[0]) * 10 + int(matches[-1]))
        return glob_sum

    def problem_2(self) -> int:
        glob_sum = 0
        wn_matches = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        for line in self.inp:
            matches = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
            for i in range(len(matches)):
                if matches[i] in wn_matches:
                    matches[i] = wn_matches[matches[i]]
            glob_sum += (int(matches[0]) * 10 + int(matches[-1]))
        return glob_sum

if __name__ == '__main__':
    print(Day01())
