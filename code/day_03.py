import numpy as np
from solutions import Solution

class Day03(Solution):
    def __init__(self):
        super().__init__(day=3, year=2023)

    def parse_input(self):
        self.arr = np.array([[c for c in row] 
                             for row in self.inp])
        self.sol_1_arr = self.arr.copy()
        self.sol_2_arr = self.arr.copy()

    def adjacencies(self, idx):
        '''
        Utility function that returns the adjacencies of a point, dealing with 
        margins of a matrix saved in `self.arr`
        '''
        for i in range(max(idx[0]-1, 0), min(idx[0]+2, len(self.arr))):
            for j in range(max(idx[1]-1, 0), min(idx[1]+2, len(self.arr[0]))):
                if not (i == idx[0] and j == idx[1]):
                    yield (i,j)

    def parse_num(self, idx, arr):
        xmin, xmax = idx[0], idx[0]; y = idx[1]
        while xmin > 0 and arr[y, xmin-1].isdigit():
            xmin -= 1
        while xmax < len(arr[0]) and arr[y, xmax].isdigit():
            xmax += 1
        n = int(''.join(arr[y, xmin:xmax]))
        return n, xmin, xmax

    def parse_number_and_replace(self, idx, arr):
        n, xmin, xmax = self.parse_num(idx, arr)
        arr[idx[1], xmin:xmax] = '.'
        return n

    def parse_numbers(self, idx, arr):
        y, x = idx; numbers = []; poss = []
        # Parse and modify temporarily
        for yj, xj in self.adjacencies((y,x)):
            if arr[yj,xj].isdigit():
                n, xmin, xmax = self.parse_num((xj,yj), arr)
                arr[yj, xmin:xmax] = '.'
                numbers.append(n)
                poss.append((yj, xmin, xmax))
        # Restore
        for i in range(len(poss)):
            p = poss[i]
            arr[p[0], p[1]:p[2]] = self.arr[p[0], p[1]:p[2]]
        return numbers

    def problem_1(self) -> int:
        tot_sum = 0
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                if not (self.sol_1_arr[i,j].isdigit() or \
                        self.sol_1_arr[i, j] == '.'):
                    # It's a symbol
                    for yj, xj in self.adjacencies((i,j)):
                        if self.sol_1_arr[yj,xj].isdigit():
                            n = self.parse_number_and_replace((xj,yj), self.sol_1_arr)
                            tot_sum += n
        return tot_sum

    def problem_2(self) -> int:
        tot_sum = 0
        for i in range(self.arr.shape[0]):
            for j in range(self.arr.shape[1]):
                if self.sol_2_arr[i,j] == '*':
                    numbers = self.parse_numbers((i,j), self.sol_2_arr)
                    if len(numbers) == 2:
                        tot_sum += (numbers[0] * numbers[1])
        return tot_sum

if __name__ == '__main__':
    print(Day03())
