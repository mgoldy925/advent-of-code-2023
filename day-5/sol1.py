import re

with open("input.txt", "r") as f:
    inp = f.read()

m = re.search("seeds:(.*)seed-to-soil map:(.*)soil-to-fertilizer map:(.*)fertilizer-to-water map:(.*)water-to-light map:(.*)light-to-temperature map:(.*)temperature-to-humidity map:(.*)humidity-to-location map:(.*)", inp, re.DOTALL)

seeds, maps = m.groups()[0], list(m.groups()[1:])
seeds = list(map(int, seeds.strip().split()))

for i, ma in enumerate(maps):
    new_map = [tuple(map(int, line.strip().split())) for line in ma.strip().splitlines()]
    maps[i] = new_map

for ma in maps:
    dest_seeds = [seed for seed in seeds]
    for i, seed in enumerate(seeds):
        for line in ma:
            d_start, s_start, rng = line
            if s_start <= seed < s_start+rng:
                dest_seeds[i] = d_start + (seed - s_start)
                break
    seeds = dest_seeds

print(min(seeds))

