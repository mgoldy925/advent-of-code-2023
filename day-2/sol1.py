qqq = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("input.txt", "r") as f:
    inp = f.readlines()

tot = 0
for line in inp:
    colid = line.index(":")
    gameid = line[4:colid]
    line = line[colid+1:-1]
    
    nope = False
    rnds = line.split(";")
    for rnd in rnds:
        amts = rnd.strip().split(", ")
        for amt in amts:
            num, col = amt.strip().split(" ")
            num = int(num)
            if num > qqq[col]:
                nope = True

    if not nope:
        tot += int(gameid)

print(tot)