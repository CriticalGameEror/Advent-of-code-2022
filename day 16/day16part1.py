with open("input.txt") as f:
    input = f.read().split()

valves = {}

isValve = False
measureFlow = False
measureCaves = False
valveLetter = ""
caves = []
rate = 0
for word in input:
    if word == "Valve":
        if measureCaves:
            measureCaves = False
            valves[valveLetter] = [rate, caves]
        isValve = True
        caves = []
    elif isValve:
        valveLetter = word
        isValve = False
        measureFlow = True
    elif "rate" in word and measureFlow:
        rate = int(word.strip("rate=;"))
        measureFlow = False
        measureCaves = True
    elif measureCaves and word not in ["tunnels", "tunnel", "leads", "lead", "to", "valves", "valve"]:
        caves.append(word.strip(","))
valves[valveLetter] = [rate, caves]





        