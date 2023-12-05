import re

words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
num_words = "|".join(words)

with open("input.txt", "r") as f:
    inp = f.readlines()

one_digit = re.compile(f"^.*(\d|{num_words}).*$")
two_digits = re.compile(f"^.*?(\d|{num_words}).*(\d|{num_words}).*?$")

total = 0
for s in inp:
    if (m := two_digits.search(s)):
        grps = m.groups()
    else:
        n = one_digit.search(s).groups()[0]
        grps = (n, n)
    total += int("".join(map(lambda x : words[x] if x in words else x, grps)))

print(total)