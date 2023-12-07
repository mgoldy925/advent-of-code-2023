from collections import Counter
from functools import cmp_to_key

def cmp(a, b):
    card_val = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    def typ(c):
        counts = Counter(c)
        nums = counts.values()
        if max(nums) == 5:
            return 6
        elif max(nums) == 4:
            return 5
        elif max(nums) == 3:
           return 4 - (len(counts) - 2)
        elif max(nums) == 2:
           return 2 - (len(counts) - 3)
        else:
            return 0

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
    print(rank, hand)
    tot += rank * hand_to_bid[hand]

print(tot)