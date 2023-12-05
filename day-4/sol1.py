import re

with open("input.txt", "r") as f:
    inp = f.read().splitlines()

tot = 0
for line in inp:
    inp1, inp2 = re.search("Card +\d+: (.*) \| (.*)", line).groups()
    winning_nums = list(map(int, inp1.split()))
    my_nums = list(map(int, inp2.split()))

    # python has no multiset, extremely sad/cringe
    wins = 0
    for num in my_nums:
        if num in winning_nums:
            wins += 1
    
    tot += int(2 ** (wins-1))

print(tot)