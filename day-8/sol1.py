import re
from itertools import cycle

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

key = "AAA"
for steps, direction in enumerate(cycle(directions), start=1):
    key = adj_list[key][direction]
    if key == "ZZZ":
        break
    
print(steps)