import re
from solutions import Solution

class Day02(Solution):
    def __init__(self):
        super().__init__(day=2, year=2023)

    def parse_input(self):
        # `self.evid` contains:
        # {game_id: [{'red': ..., 'blue': ..., 'green': ...}, 
        #            {'red': ..., 'blue': ..., 'green': ...}, 
        #             ...],
        # ...}
        self.evid = {}
        for line in self.inp:
            ## Parse string
            game_id = int(re.search(r'Game (\d+)', line).group(1))
            shown = re.findall(r'(\d+) (blue|red|green)(,|;|)', line)
            ## Add first set to game_id
            self.evid[game_id] = [{'red': 0, 'green': 0, 'blue': 0}]
            current_set = 0
            for cubes in shown:
                ## Add evidence for set
                self.evid[game_id][current_set][cubes[1]] += int(cubes[0])
                ## When done, change set
                if cubes[2] == ';':
                    self.evid[game_id].append({'red': 0, 'green': 0, 'blue': 0})
                    current_set += 1

    def problem_1(self) -> int:
        sum_games = 0
        constraint = {'red': 12, 'green': 13, 'blue': 14}
        for game_id in self.evid:
            # Check if for any of the sets in the game some evidence 
            # breaks the constraints
            if not any([game_set[x] > constraint[x]
                        for game_set in self.evid[game_id]
                        for x in constraint]):
                # If not, add the game_id to the sum
                sum_games += game_id
        return sum_games

    def problem_2(self) -> int:
        sum_power_min_sets = 0
        for game_id in self.evid:
            mins = {
                color: max([
                    game_set[color] 
                    for game_set in self.evid[game_id]
                ]) 
                for color in ['red', 'green', 'blue']
            }
            sum_power_min_sets += (mins['red'] * mins['green'] * mins['blue'])
        return sum_power_min_sets

if __name__ == '__main__':
    print(Day02())
