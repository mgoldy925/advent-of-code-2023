from collections import Counter
from functools import cmp_to_key

def cmp(a, b):
    card_val = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        'J': 1
    }

    def typ(c):
        counts = Counter(c)
        nums = counts.values()
        if max(nums) == 5:
            val = 6
        elif max(nums) == 4:
            val = 5
        elif max(nums) == 3:
            val = 4 - (len(counts) - 2)
        elif max(nums) == 2:
            val = 2 - (len(counts) - 3)
        else:
            val = 0
        
        jokers = counts["J"]
        if jokers:
            if val == 0:
                val += 1
            elif val == 1:
                val += 2
            elif val == 2:
                val += 2 if jokers == 1 else 3
            elif val == 3:
                val += 2
            elif val == 4:
                val += 2
            elif val == 5:
                val += 1
        return val

    ra, rb = typ(a), typ(b)
    if ra != rb:
        return ra - rb

    for ca, cb in zip(a, b):
        if ca != cb:
            return card_val[ca] - card_val[cb]
    
    return 0

with open("input.txt", "r") as f:
    inp = f.read().splitlines()

inp = [line.split() for line in inp]
hand_to_bid = {hand: int(bid) for hand, bid in inp}
hands = sorted(hand_to_bid, key=cmp_to_key(cmp))

tot = 0
for rank, hand in enumerate(hands, start=1):
    tot += rank * hand_to_bid[hand]

print(tot)