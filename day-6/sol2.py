from math import sqrt, ceil, floor

with open("input.txt", "r") as f:
    inp = f.read().splitlines()

t = int(''.join(inp[0].split()[1:]))
d = int(''.join(inp[1].split()[1:]))

sq = sqrt(t*t - 4*d)
t1, t2 = ceil((t - sq) / 2), floor((t + sq) / 2)
l, r = max(1, t1), min(t, t2)
print(r - l + 1 if l * r != d else r - l - 1)