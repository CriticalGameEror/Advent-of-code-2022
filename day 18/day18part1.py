with open("input.txt") as f:
    input = f.read().split()

for cube in range(len(input)):
    input[cube] = input[cube].split(",")

cordSet = set()
for cube in input:
    cordSet.add((int(cube[0]), int(cube[1]), int(cube[2])))

total = 0
for cube in input:
    sides = 6
    x = int(cube[0])
    y = int(cube[1])
    z = int(cube[2])
    if (x+1, y, z) in cordSet:
        sides -= 1
    if (x-1, y, z) in cordSet:
        sides -= 1
    if (x, y+1, z) in cordSet:
        sides -= 1
    if (x, y-1, z) in cordSet:
        sides -= 1
    if (x, y, z+1) in cordSet:
        sides -= 1
    if (x, y, z-1) in cordSet:
        sides -= 1
    total += sides
print(total)

