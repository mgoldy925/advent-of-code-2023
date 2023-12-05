import re
from collections import defaultdict

sym_regex = "#|\\$|%|&|\\+|-|/|=|@"
symbol = "!"
ast = "*"

with open("input.txt", "r") as f:
    eng = f.read()

eng = re.sub(sym_regex, symbol, eng).splitlines()
eng_arr = [list(line) for line in eng]
gears = defaultdict(list)

rows = len(eng)
for row, line in enumerate(eng):
    cols = len(line)

    matches = re.finditer("(\d+)", line)
    for match in matches:
        num = int(match.group())
        start, end = match.span()

        sr, er = max(0, row-1), min(rows-1, row+1)
        sc, ec = max(0, start-1), min(cols-1, end)
        # box = eng_np[sr:er+1, sc:ec+1]
        # prob a more numpy-y way to do this
        for i in range(sr, er+1):
            for j in range(sc, ec+1):
                if eng_arr[i][j] == ast:
                    gears[(i,j)].append(num)

tot = 0
for adj_nums in gears.values():
    if len(adj_nums) == 2:
        tot += adj_nums[0] * adj_nums[1]

print(tot)