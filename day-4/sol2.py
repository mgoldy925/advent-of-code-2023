import re

with open("input.txt", "r") as f:
    inp = f.read().splitlines()

n = len(inp)
copies = [1 for _ in range(n+1)]  # is using an iterator over inp more expensive?
copies[0] = 0
for line in inp:
    card_inp, inp1, inp2 = re.search("Card +(\d+): (.*) \| (.*)", line).groups()
    card_num = int(card_inp)
    winning_nums = list(map(int, inp1.split()))
    my_nums = list(map(int, inp2.split()))

    # python has no multiset, extremely sad/cringe
    wins = 0
    for num in my_nums:
        if num in winning_nums:
            wins += 1

    for card in range(card_num+1, card_num+1+wins):
        copies[card] += copies[card_num]

    # print(copies[card_num])
print(copies)
print(sum(copies))