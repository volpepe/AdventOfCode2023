import re
from solutions import Solution

class Day06(Solution):
    def __init__(self):
        super().__init__(day=6, year=2023)

    def compute_distance(self, hold_time, tot_time):
        run_time = tot_time - hold_time
        return run_time * hold_time
    
    def count_ways_to_win(self, tot_time, tot_dist):
        ways_to_win = 0
        for h in range(tot_time):
            if self.compute_distance(h, tot_time) > tot_dist:
                ways_to_win += 1
        return ways_to_win

    def parse_input(self):
        ts, ds = re.findall(r'\d+', self.inp[0]), re.findall(r'\d+', self.inp[1])
        self.times = [int(x) for x in ts]
        self.distances = [int(x) for x in ds]
        self.real_time = int(''.join(ts))
        self.real_distance = int(''.join(ds))

    def problem_1(self) -> None:
        tot_ = 1
        for i in range(len(self.times)):
            t = self.times[i]
            d = self.distances[i]
            tot_ *= self.count_ways_to_win(t, d)
        return tot_
    
    def problem_2(self) -> None:
        # Inefficient (like 10s) but it solves the thing
        return self.count_ways_to_win(self.real_time, self.real_distance)

if __name__ == '__main__':
    print(Day06())