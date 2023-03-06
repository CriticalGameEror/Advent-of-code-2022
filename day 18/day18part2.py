with open("input.txt") as f:
    input = f.read().split()

for cube in range(len(input)):
    input[cube] = input[cube].split(",")


#TODO add back in air pocket check to make sure that the sorrounding cubes are 
cordSet = set()
airSet = set()
lowestX = None
highestX = None
lowestY = None
highestY = None
lowestZ = None
highestZ = None
for cube in input:
    x = int(cube[0])
    y = int(cube[1])
    z = int(cube[2])
    cordSet.add((x, y, z))
    if highestX == None:
        highestX = x
    elif x > highestX:
        highestX = x
    if highestY == None:
        highestY = y
    elif y > highestY:
        highestY = y
    if highestZ == None:
        highestZ = z
    elif z > highestZ:
        highestZ = z
    if lowestX == None:
        lowestX = x
    elif x < lowestX:
        lowestX = x
    if lowestY == None:
        lowestY = y
    elif y < lowestY:
        lowestY = y
    if lowestZ == None:
        lowestZ = z
    elif z < lowestZ:
        lowestZ = z

for x in range(lowestX, highestX+1):
    for y in range(lowestY, highestY+1):
        for z in range(lowestZ, highestZ+1):
            if (x,y,z) not in cordSet:
                airSet.add((x,y,z))

total = 0
for cube in input:
    sides = 6
    x = int(cube[0])
    y = int(cube[1])
    z = int(cube[2])
    if (x+1, y, z) in cordSet or (x+1, y, z) in airSet:
        sides -= 1
    if (x-1, y, z) in cordSet or (x-1, y, z) in airSet:
        sides -= 1
    if (x, y+1, z) in cordSet or (x, y+1, z) in airSet:
        sides -= 1
    if (x, y-1, z) in cordSet or (x, y-1, z) in airSet:
        sides -= 1
    if (x, y, z+1) in cordSet or (x, y, z+1) in airSet:
        sides -= 1
    if (x, y, z-1) in cordSet or (x, y, z-1) in airSet:
        sides -= 1
    
    total += sides
print(total)

