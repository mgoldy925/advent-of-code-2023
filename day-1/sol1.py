import re

with open("input.txt", "r") as f:
    inp = f.readlines()

one_digit = re.compile("^.*(\d).*$")
two_digits = re.compile("^.*?(\d).*(\d).*?$")

total = 0
for s in inp:
    if (m := two_digits.search(s)):
        grps = m.groups()
    else:
        n = one_digit.search(s).groups()[0]
        grps = (n, n)
    total += int("".join(grps))

print(total)