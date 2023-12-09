import re
from itertools import cycle
import math

adj_list = {}
with open("input.txt", "r") as f:
    directions = f.readline().strip()

    f.readline()
    pattern = re.compile("([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)")
    for line in f.read().splitlines():
        key, left, right = pattern.search(line).groups()
        adj_list[key] = {
            "L": left,
            "R": right
        }

a_strs = [s for s in adj_list if s[-1] == "A"]
# z_strs = [s for s in adj_list if s[-1] == "Z"]

cycle_lengths = []
for a_str in a_strs:
    key = a_str
    for steps, direction in enumerate(cycle(directions), start=1):
        key = adj_list[key][direction]
        if key[-1] == "Z":
            cycle_lengths.append(steps)
            break

tot_steps = math.lcm(*cycle_lengths)
print(tot_steps)