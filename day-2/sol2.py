with open("input.txt", "r") as f:
    inp = f.readlines()

tot = 0
for line in inp:
    colid = line.index(":")
    gameid = line[4:colid]
    line = line[colid+1:-1]
    
    mins = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    rnds = line.split(";")
    for rnd in rnds:
        amts = rnd.strip().split(", ")
        for amt in amts:
            num, col = amt.strip().split(" ")
            num = int(num)
            mins[col] = max(mins[col], num)

    tot += mins["red"] * mins["green"] * mins["blue"]

print(tot)