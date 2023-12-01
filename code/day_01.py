import re
from typing import List
from get_input import get_input

def problem_1(inp: List[str]):
    glob_sum = 0
    for line in inp:
        matches = re.findall(r'\d', line)
        glob_sum += (int(matches[0]) * 10 + int(matches[-1]))
    return glob_sum

def problem_2(inp: List[str]):
    glob_sum = 0
    wn_matches = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                  'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for line in inp:
        matches = re.finditer(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        matches = [match.group(1) for match in matches]
        for i in range(len(matches)):
            if matches[i] in wn_matches:
                matches[i] = wn_matches[matches[i]]
        glob_sum += (int(matches[0]) * 10 + int(matches[-1]))
    return glob_sum

if __name__ == '__main__':
    inp = get_input(1, 2023)
    sol_1 = problem_1(inp)
    print(f"Solution to problem 1: {sol_1}")
    sol_2 = problem_2(inp)
    print(f"Solution to problem 2: {sol_2}")
