import re
from collections import deque

with open("input.txt", "r") as f:
    inp = f.read()

m = re.search("seeds:(.*)seed-to-soil map:(.*)soil-to-fertilizer map:(.*)fertilizer-to-water map:(.*)water-to-light map:(.*)light-to-temperature map:(.*)temperature-to-humidity map:(.*)humidity-to-location map:(.*)", inp, re.DOTALL)

seeds, maps = m.groups()[0], list(m.groups()[1:])

seeds = list(map(int, seeds.strip().split()))
seed_groups = []
for i in range(len(seeds)//2):
    seed_groups.append((seeds[2*i], seeds[2*i+1]))
seeds = seed_groups

for i, ma in enumerate(maps):
    tmp_map = [tuple(map(int, line.strip().split())) for line in ma.strip().splitlines()]
    new_map = {}
    for d, s, r in tmp_map:
        new_map[(s, r)] = (d, r)
    maps[i] = new_map

for ma in maps:
    dest_seeds = []

    for cur_seed_rng in seeds:
        cur_seeds = set([cur_seed_rng])

        for s, sr in ma:
            for seed_pair in list(cur_seeds):
                seed_start, seed_rng = seed_pair

                if s <= seed_start < s + sr or seed_start <= s < seed_start + seed_rng:
                    cur_seeds.remove(seed_pair)

                    lend, rend = max(seed_start, s), min(seed_start + seed_rng, s + sr)
                    d, dr = ma[(s, sr)]
                    dest_seeds.append((d + (lend - s), (rend - lend)))

                    if lend > seed_start:
                        cur_seeds.add((seed_start, lend - seed_start))
                    if rend < seed_start + seed_rng:
                        cur_seeds.add((rend, seed_start + seed_rng - rend))
        
        dest_seeds.extend(list(cur_seeds))

    seeds = dest_seeds

print(min([st for st, _ in seeds]))

