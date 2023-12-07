from math import sqrt, ceil, floor

with open("input.txt", "r") as f:
    inp = f.read().splitlines()

prod = 1
for t, d in zip(inp[0].split()[1:], inp[1].split()[1:]):
    T, D = int(t), int(d)
    sq = sqrt(T*T - 4*D)
    t1, t2 = -((sq - T) // 2), (T + sq) // 2
    l, r = max(1, t1), min(T, t2)
    prod *= r - l + 1 if l * r != D else r - l - 1

print(prod)