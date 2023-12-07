from collections import Counter

card_let = {
    'A': 'M',
    'K': 'L',
    'Q': 'K',
    'T': 'J',
    '9': 'I',
    '8': 'H',
    '7': 'G',
    '6': 'F',
    '5': 'E',
    '4': 'D',
    '3': 'C',
    '2': 'B',
    'J': 'A'
}

def val(c):
    counts = Counter(c)
    j_counts = counts["J"]
    del counts["J"]
    l = sorted(counts.values() if counts else [0], reverse=True)
    l.append(''.join(card_let[ch] for ch in c))
    l[0] += j_counts
    return l

with open("input.txt", "r") as f:
    inp = f.read().splitlines()

inp = [line.split() for line in inp]
hand_to_bid = {hand: int(bid) for hand, bid in inp}
hands = sorted(hand_to_bid, key=val)

tot = 0
for rank, hand in enumerate(hands, start=1):
    tot += rank * hand_to_bid[hand]

print(tot)