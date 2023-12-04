import re
from solutions import Solution

class Day04(Solution):
    def __init__(self):
        super().__init__(day=4, year=2023)

    def parse_input(self):
        self.inp_dict = {}
        for line in self.inp:
            card = line.split(':')[0]
            winners = line.split(':')[1].split('|')[0]
            numbers = line.split('|')[1]
            card = int(re.findall(r'\d+', card)[0])
            winners = [int(x) for x in re.findall(r'\d+', winners)]
            numbers = [int(x) for x in re.findall(r'\d+', numbers)]
            self.inp_dict[card] = {'win': winners, 'num': numbers, 'amount': 1}

    def problem_1(self) -> int:
        tot_sum = 0
        for t in self.inp_dict:
            cur_points = 0
            wins = self.inp_dict[t]['win']
            nums = set(self.inp_dict[t]['num'])
            for w in wins:
                if w in nums:
                    cur_points = (cur_points * 2) if cur_points > 0 else 1
            tot_sum += cur_points
        return tot_sum

    def problem_2(self) -> int:
        for t in self.inp_dict:
            cur_points = 0
            wins = self.inp_dict[t]['win']
            nums = set(self.inp_dict[t]['num'])
            for w in wins:
                if w in nums:
                    cur_points += 1
            if cur_points > 0:
                for k in range(t+1, t+1+cur_points):
                    self.inp_dict[k]['amount'] += self.inp_dict[t]['amount']
        return sum(self.inp_dict[x]['amount'] 
                   for x in self.inp_dict)

if __name__ == '__main__':
    print(Day04())
