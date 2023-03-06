with open("input.txt") as f:
    input = f.read().split()

# the sets contains the boundaries of the maze
boundariesX = {0, len(input[0])-1}
boundariesY = {0, len(input)-1}
    
def move(pos, direct):
    if direct == "U":
        if pos[0]-1 in boundariesY:
            pos = (len(input)-2, pos[1])
        else:
            pos = (pos[0]-1, pos[1])
    elif direct == "R":
        if pos[1]+1 in boundariesX:
            pos = (pos[0], 1)
        else:
            pos = (pos[0], pos[1]+1)
    elif direct == "D":
        if pos[0]+1 in boundariesY:
            pos = (1, pos[1])
        else:
            pos = (pos[0]+1, pos[1])
    else:
        if pos[1]-1 in boundariesX:
            pos = (pos[0], len(input[0])-2)
        else:
            pos = (pos[0], pos[1]-1)
    return pos

storms = set()
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == "^":
            storms.add(((y,x), "U"))
        elif input[y][x] == ">":
            storms.add(((y,x), "R"))
        elif input[y][x] == "v":
            storms.add(((y,x), "D"))
        elif input[y][x] == "<":
            storms.add(((y,x), "L"))

shortest = None # the current shortest path
visited = set() # contains when a location was visited at a particular time
end = (len(input)-1, len(input[-1])-2) # the end of the maze

def findShortest(currentPos, targetMove, storms, currentShortest=0): 
    global shortest, visited
    
    #print(currentPos, targetMove, currentShortest)
    
    if (targetMove, currentShortest) in visited:
        return

    if targetMove[0] in boundariesY or targetMove[1] in boundariesX:
        if targetMove != (0,1) or targetMove != end:
            return
    
    # moves the storms
    newStorms = []
    for storm in storms:
        newStorms.append((move(storm[0], storm[1]), storm[1]))
    storms = set(newStorms).copy()

    currentPos = targetMove # moves the player
    
    # if the character is in a storm
    for storm in storms:
        if currentPos == storm[0]:
            return

    visited.add((currentPos, currentShortest))
    
    # checks if character has reached the end
    if currentPos == end:
        if shortest == None:
            shortest = currentShortest
        elif currentShortest < shortest:
            shortest = currentShortest
        return

    currentShortest += 1

    # if the current path is longer than the shortest path
    if shortest != None:
        if currentShortest >= shortest:
            return

    findShortest(currentPos, (currentPos[0], currentPos[1]-1), storms.copy(), currentShortest) # move left
    findShortest(currentPos, (currentPos[0], currentPos[1]+1), storms.copy(), currentShortest) # move right
    findShortest(currentPos, (currentPos[0]-1, currentPos[1]), storms.copy(), currentShortest) # move up
    findShortest(currentPos, (currentPos[0]+1, currentPos[1]), storms.copy(), currentShortest) # move down
    findShortest(currentPos, (currentPos[0], currentPos[1]), storms.copy(), currentShortest) # wait
    

findShortest((0,1), (1,1), storms.copy()) # move down
#findShortest((0,1), (0,1), storms.copy()) # wait
print(shortest)
    



