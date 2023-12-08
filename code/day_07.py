import re
from solutions import Solution

class Day07(Solution):
    def __init__(self):
        self.map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
                    '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
                    '3': 3, '2': 2}
        self.map2 = {'A': 14, 'K': 13, 'Q': 12, 'T': 10,
                    '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
                    '3': 3, '2': 2, 'J': 1}
        super().__init__(day=7, year=2023)

    def process_hand(self, hand, sol=1):
        m = self.map if sol == 1 else self.map2
        return [m[h] for h in hand]
    
    def check_type(self, hand, sol=1):
        count = {
            t: len([h for h in hand if h == t])
            for t in hand
        }

        # Patch for 2nd part: add 1s to most frequent count
        if sol == 2:
            if 1 in count:
                no_ones = [x for x in count if x != 1]
                if len(no_ones) > 0:
                    num_1s = count[1]
                    max_count = max(no_ones, key=lambda x: count[x])
                    count[max_count] += num_1s
                    del count[1]

        ct = count.values()

        # five of a kind     --> 7
        if len(ct) == 1: return 7
        elif len(ct) == 2:
            # four of a kind --> 6
            if any([x == 4 for x in ct]): return 6
            # full house     --> 5
            else: return 5
        elif len(ct) == 3:
            # three of a kind--> 4
            if any([x == 3 for x in ct]): return 4
            # two pair       --> 3
            else: return 3
        # one pair           --> 2
        elif len(ct) == 4: return 2
        # high card          --> 1
        else: return 1

    def setup(self, sol=1):
        hands, types, bids = [], [], []

        for l in self.inp:
            hstr, bid = re.match(r'(.....) (\d+)', l).groups()
            bid = int(bid)
            hand = self.process_hand(hstr, sol)
            hand_type = self.check_type(hand, sol)
            hands.append(hand), types.append(hand_type); bids.append(bid)

        # Sort by type or cards
        hands_to_values = [types[i]*(15**5) + h[0]*(15**4) + h[1]*(15**3) + h[2]*(15**2) + h[3]*15 + h[4]
                           for i, h in enumerate(hands)]
        
        self.sol_setup[f'sol_{sol}']['hands'] = [h for (_, h) in sorted(zip(hands_to_values, hands), key=lambda x: -x[0])]
        self.sol_setup[f'sol_{sol}']['types'] = [t for (_, t) in sorted(zip(hands_to_values, types), key=lambda x: -x[0])]
        self.sol_setup[f'sol_{sol}']['bids']  = [b for (_, b) in sorted(zip(hands_to_values, bids), key=lambda x: -x[0])]

    def parse_input(self):
        self.sol_setup = {
            'sol_1': {
                'hands': [], 'types': [], 'bids': []
            },
            'sol_2': {
                'hands': [], 'types': [], 'bids': []
            }
        }
        self.setup(sol=1)
        self.setup(sol=2)

    def problem_1(self) -> None: 
        b = self.sol_setup['sol_1']['bids']
        return sum([b[i] * (len(b)-i) for i in range(len(b))])

    def problem_2(self) -> None:
        b = self.sol_setup['sol_2']['bids']
        return sum([b[i] * (len(b)-i) for i in range(len(b))])

if __name__ == '__main__':
    print(Day07())