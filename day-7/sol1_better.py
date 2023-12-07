from collections import Counter

card_let = {
    'A': 'M',
    'K': 'L',
    'Q': 'K',
    'J': 'J',
    'T': 'I',
    '9': 'H',
    '8': 'G',
    '7': 'F',
    '6': 'E',
    '5': 'D',
    '4': 'C',
    '3': 'B',
    '2': 'A'
}

def val(c):
    counts = sorted(Counter(c).values(), reverse=True)
    counts.append(''.join(card_let[ch] for ch in c))
    return counts

with open("input.txt", "r") as f:
    inp = f.read().splitlines()

inp = [line.split() for line in inp]
hand_to_bid = {hand: int(bid) for hand, bid in inp}
hands = sorted(hand_to_bid, key=val)

tot = 0
for rank, hand in enumerate(hands, start=1):
    tot += rank * hand_to_bid[hand]

print(tot)