import re
from solutions import Solution

DIRECT = {'L': 0, 'R': 1}

class Day08(Solution):
    def __init__(self):
        super().__init__(day=8, year=2023)

    def parse_instructions(self, inst):
        return [DIRECT[x] for x in inst]
    
    def parse_network(self, lines):
        graph = {}
        for line in lines:
            node, left, right = re.match(r'(...) = \((...), (...)\)', line).groups()
            graph[node] = (left, right)
        return graph

    def parse_input(self):
        self.instr = self.parse_instructions(self.inp[0])
        self.graph = self.parse_network(self.inp[2:])

    def problem_1(self) -> int:
        cur_node  = 'AAA'
        cur_instr = 0
        while cur_node != 'ZZZ':
            instr = self.instr[cur_instr % len(self.instr)]
            cur_node = self.graph[cur_node][instr]
            cur_instr += 1
        return cur_instr

    def find_end_node(self, cur_node):
        cur_instr = 0
        while cur_node[-1] != 'Z':
            instr = self.instr[cur_instr % len(self.instr)]
            cur_node = self.graph[cur_node][instr]
            cur_instr += 1
        return cur_instr

    def problem_2(self) -> int:
        cur_nodes = [x for x in self.graph if x[-1] == 'A']
        end_node_idxs = []
        for node in cur_nodes:
            idx_end_node = self.find_end_node(node)
            end_node_idxs.append(idx_end_node)
        lcm = end_node_idxs[0]
        for i in range(1, len(end_node_idxs)):
            lcm = self.least_common_denominator(lcm, end_node_idxs[i])
        return lcm

    def least_common_denominator(self, n1, n2) -> int:
        return n1 * n2 // self.greatest_common_divisor(n1, n2)

    def greatest_common_divisor(self, n1, n2) -> int:
        a, b = (n1, n2) if n1 > n2 else (n2, n1)    # a > b
        return a if b == 0 else self.greatest_common_divisor(b, a % b)

if __name__ == '__main__':
    print(Day08())