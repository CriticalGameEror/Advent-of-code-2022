with open("input.txt") as f:
    input = f.read().split()

elves = set()
lowestY = 999999999999
highestY = -999999999999
lowestX = 999999999999
highestX = -999999999999

for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == "#":
            elves.add((y,x))

directionQueue = ["N", "S", "W", "E"] # the priority of moving for the elves
for round in range(10):
    moves = {} # key being where the elf will move and the value being where the elf current is
    duplicates = set() # contains where duplicate movements were detected

    # decides what direction to move in
    for elf in elves:     
        # checks for the positions around the elf
        sorround = {"N": None, "NE": None, "E": None, "SE": None, "S": None, "SW": None, "W": None, "NW": None} # positions around the elf
        for y in [-1,0,1]:
            for x in [-1,0,1]:
                if y == 0 and x == 0:
                    continue
                elif (elf[0]+y, elf[1]+x) in elves:
                    dir = ""
                    if y == 1 and x == 0:
                        dir = "S"
                    elif y == 1 and x == 1:
                        dir = "SE"
                    elif y == 0 and x == 1:
                        dir = "E"
                    elif y == -1 and x == 1:
                        dir = "NE"
                    elif y == -1 and x == 0:
                        dir = "N"
                    elif y == -1 and x == -1:
                        dir = "NW"
                    elif y == 0 and x == -1:
                        dir = "W"
                    elif y == 1 and x == -1:
                        dir = "SW"

                    sorround[dir] = (elf[0]+y, elf[1]+x)

        # checks that there is an elf sorrounding the elf
        noSorround = True
        for otherElf in sorround:
            if sorround[otherElf] != None:
                noSorround = False
                break
        if noSorround:
            continue

        
        # deciding what direction to move
        for direction in directionQueue:
            if direction == "N":
                if sorround["NW"] == None and sorround["N"] == None and sorround["NE"] == None:
                    if (elf[0]-1, elf[1]) in moves or (elf[0]-1, elf[1]) in duplicates:
                        duplicates.add((elf[0]-1, elf[1]))
                        del(moves[(elf[0]-1, elf[1])])
                    else:
                        moves[(elf[0]-1, elf[1])] = elf
                    break
            elif direction == "S":
                if sorround["SE"] == None and sorround["S"] == None and sorround["SW"] == None:
                    if (elf[0]+1, elf[1]) in moves or (elf[0]+1, elf[1]) in duplicates:
                        duplicates.add((elf[0]+1, elf[1]))
                        del(moves[(elf[0]+1, elf[1])])
                    else:
                        moves[(elf[0]+1, elf[1])] = elf
                    break
            elif direction == "W":
                if sorround["SW"] == None and sorround["W"] == None and sorround["NW"] == None:
                    if (elf[0], elf[1]-1) in moves or (elf[0], elf[1]-1) in duplicates:
                        duplicates.add((elf[0], elf[1]-1))
                        del(moves[(elf[0], elf[1]-1)])
                    else:
                        moves[(elf[0], elf[1]-1)] = elf
                    break
            else:
                if sorround["NE"] == None and sorround["E"] == None and sorround["SE"] == None:
                    if (elf[0], elf[1]+1) in moves or (elf[0], elf[1]+1) in duplicates:
                        duplicates.add((elf[0], elf[1]+1))
                        del(moves[(elf[0], elf[1]+1)])
                    else:
                        moves[(elf[0], elf[1]+1)] = elf
                    break

    # move the elves
    for move in moves:
        elves.discard(moves[move])
        elves.add(move)
    
    # takes the first direction and moves it to the back of the queue
    item = directionQueue.pop(0)
    directionQueue.append(item)

# check for the lowest and highest x/y values
for elf in elves:
    if elf[0] > highestY:
        highestY = elf[0]
    if elf[0] < lowestY:
        lowestY = elf[0]
    if elf[1] > highestX:
        highestX = elf[1]
    if elf[1] < lowestX:
        lowestX = elf[1]

total = 0
# checks for empty spaces
for y in range(lowestY, highestY+1):
    for x in range(lowestX, highestX+1):
        if (y,x) not in elves:
            total += 1

#print(highestX, lowestX)
print(total)