import re
from solutions import Solution

class Day05(Solution):
    def __init__(self):
        super().__init__(day=5, year=2023)

    def parse_input(self):
        self.seeds = []
        self.seed_to_soil = {}
        self.soil_to_fertilizer = {}
        self.fertilizer_to_water = {}
        self.water_to_light = {}
        self.light_to_temperature = {}
        self.temperature_to_humidity = {}
        self.humidity_to_location = {}
        self.dict_dict = {
            'seed-to-soil': self.seed_to_soil,
            'soil-to-fertilizer': self.soil_to_fertilizer,
            'fertilizer-to-water': self.fertilizer_to_water,
            'water-to-light': self.water_to_light,
            'light-to-temperature': self.light_to_temperature,
            'temperature-to-humidity': self.temperature_to_humidity,
            'humidity-to-location': self.humidity_to_location
        }
        self.dict_sequence = list(self.dict_dict.keys())
        self.inverted_dict_sequence = self.dict_sequence[::-1]

        i = 0
        while i < len(self.inp):
            if 'seeds' in self.inp[i]:
                self.seeds = [int(x) for x in re.findall(r'\d+', self.inp[i])]
            else:
                for key in self.dict_dict:
                    if key in self.inp[i]:
                        while (i+1) < len(self.inp) and self.inp[i+1] != '':
                            i+=1
                            self.populate_map(self.dict_dict[key], i)
            i+=1

        # We should ignore one every two seeds
        self.actual_seeds = self.seeds[::2]
        self.actual_seeds_ranges = self.seeds[1::2]

    def populate_map(self, map, i):
        trg, src, rng = re.findall(r'\d+', self.inp[i])
        trg, src, rng = int(trg), int(src), int(rng)
        map[src] = (trg, rng)

    def find_in_map(self, el, map):
        for k in map:
            rng = map[k][1]
            if k <= el < (k + rng):
                return map[k][0] + (el-k)
        else:
            return el
        
    def get_range_for_val(self, val, map):
        for k in map:
            if k <= val < (k + map[k][1]):
                return (map[k][0] + (val - k), (map[k][0] + map[k][1]))
        return None
        
    def map_range(self, rng, map):
        srt, end = rng
        out_rngs = []
        # Check which ranges in the map intersecate the input range
        i = srt
        while i < end:
            map_range = self.get_range_for_val(i, map)
            if map_range is None:
                # Move to the first available element
                old_i = i
                if i < max(map.keys()):
                    i = min([x for x in map.keys() if x > i])
                else:
                    i = end
                out_rngs.append((old_i, i))
            else:
                srt_map_rng, end_map_rng = map_range
                end_map_rng = srt_map_rng + min((end_map_rng - srt_map_rng), (end - i))
                out_rngs.append((srt_map_rng, end_map_rng))
                i += (end_map_rng - srt_map_rng)
        return out_rngs

    def problem_1(self) -> int:
        locations = []
        for seed in self.seeds:
            nextval = seed
            for map_name in self.dict_sequence:
                nextval = self.find_in_map(nextval, self.dict_dict[map_name])
            locations.append(nextval)
        return min(locations)

    def problem_2(self) -> int:
        # Mapping ranges to ranges
        min_locations = []
        for i in range(len(self.actual_seeds)):
            next_rngs = [(self.actual_seeds[i], self.actual_seeds[i] + self.actual_seeds_ranges[i])]
            for map_name in self.dict_sequence:
                tmp_next_rngs = []
                for rng in next_rngs:
                    tmp_next_rngs.extend(self.map_range(rng, self.dict_dict[map_name]))
                next_rngs = tmp_next_rngs
            min_locations.append(min(x[0] for x in next_rngs))
        return min(min_locations)

if __name__ == '__main__':
    print(Day05())
