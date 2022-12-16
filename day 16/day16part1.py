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

def findDistances(valve, total=0, visited=[], distances={}):
    visited.append(valve)
    for v in valves[valve][1]:
        if v not in visited:
            distances[v] = total+1
    
    return distances

for valve in valves:
    valves[valve].append(findDistances(valve))

print(valves["BB"])