import re
import numpy as np

sym_regex = "#|\\$|%|&|\\*|\\+|-|/|=|@"
symbol = "!"

with open("input.txt", "r") as f:
    eng = f.read()

tot = 0
eng = re.sub(sym_regex, symbol, eng).splitlines()
eng_np = np.array([list(line) for line in eng])

rows = len(eng)
for row, line in enumerate(eng):
    cols = len(line)

    matches = re.finditer("(\d+)", line)
    for match in matches:
        start, end = match.span()

        sr, er = max(0, row-1), min(rows-1, row+1)
        sc, ec = max(0, start-1), min(cols-1, end)
        box = eng_np[sr:er+1, sc:ec+1]

        if symbol in box:
            tot += int(match.group())

print(tot)