with open("input.txt") as f:
    input = f.readlines()

class Node():
    def __init__(self, wall, y, x) -> None:
        self.wall = wall # wall or not
        self.row = x
        self.column = y

# removes any new line chars
for x in range(len(input)):
    input[x] = input[x].strip("\n")

instructionsRaw = input.pop(-1) # removes the instructions from the input
input.pop(-1) # ensures that only the maze reamins 

# formats the instructions into a list
def formatInstruc():
    instructions = []
    numb = ""
    for instruction in instructionsRaw:
        if instruction not in ["L", "R"]:
            numb += instruction
            continue
        instructions.append(int(numb))
        numb = ""
        instructions.append(instruction)
    if numb != "":
        instructions.append(int(numb))

    return instructions

insructions = formatInstruc()

def addLoopX(loopCords, loopXQueued, y, x):
    if len(loopXQueued) != 1:
        loopXQueued.append((y,x))
    else:
        loopXQueued.append((y,x))
        loopCords[loopXQueued[0]] = loopXQueued[1]
        loopCords[loopXQueued[1]] = loopXQueued[0]
        loopXQueued = []
    
    return loopCords, loopXQueued

def addLoopY(loopCords, loopYQueued, y, x):
    loopYQueued.add((y,x))
    currentYCord = [] # list of all possible looping cords for the current x value
    for tempY in range(len(input)):
        if (tempY, x) in loopYQueued:
            currentYCord.append((tempY,x))
        if len(currentYCord) == 2:
            loopYQueued.discard(currentYCord[0])
            loopYQueued.discard(currentYCord[1])
            loopCords[currentYCord[0]] = currentYCord[1]
            loopCords[currentYCord[1]] = currentYCord[0]
            currentYCord = []

    return loopCords, loopYQueued


def formatMaze():
    loopCordsX = {} # y cords and what y cord value they loop around to 
    loopCordsY = {} # x cords and what x cord value they loop around to
    nodes = {} # node object with the coords as the key (key in the form (y,x))

    loopYQueued = set() # for any y values that are a wrap around
    loopXQueued = [] # for any x values that are a wrap around

    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == ".":
                nodes[(y,x)] = Node(False, y, x)
            elif input[y][x] == "#":
                nodes[(y,x)] = Node(True, y, x)
            else:
                continue
            
            # check x looping values
            if x-1 < 0 or x+1 >= len(input[y]):
                loopCordsX, loopXQueued = addLoopX(loopCordsX, loopXQueued, y, x)
            elif input[y][x-1] == " " or input[y][x+1] == " ":
                loopCordsX, loopXQueued = addLoopX(loopCordsX, loopXQueued, y, x)

            # check for y looping values
            if y+1 >= len(input) or y-1 < 0:
                loopCordsY, loopYQueued = addLoopY(loopCordsY, loopYQueued, y, x)
            elif x >= len(input[y-1]) or x >= len(input[y+1]): # if the x value is too high (therefore meaning that its an emtpy space)
                loopCordsY, loopYQueued = addLoopY(loopCordsY, loopYQueued, y, x)
            elif input[y+1][x] == " " or input[y-1][x] == " ":
                loopCordsY, loopYQueued = addLoopY(loopCordsY, loopYQueued, y, x)
        
    return loopCordsX, loopCordsY, nodes

loopCordsX, loopCordsY, nodes = formatMaze()

# finds the starting position of the maze
def findStartingPosX():
    for x in range(len(input[0])):
        if input[0][x] == "." or input[0][x] == "#":
            return x

direction = "R" # the current direction being faced
currentPos = (0, findStartingPosX())

for instruction in insructions:
    if instruction in ["R", "L"]:
        if direction == "R":
            if instruction == "R":
                direction = "D"
            else:
                direction = "U"
        elif direction == "U":
            if instruction == "R":
                direction = "R"
            else:
                direction = "L"
        elif direction == "L":
            if instruction == "R":
                direction = "U"
            else:
                direction = "D"
        else:
            if instruction == "R":
                direction = "L"
            else:
                direction = "R"
    
    else:
        for move in range(instruction):
            moveTo = currentPos
            if direction == "R":
                if (moveTo[0], moveTo[1]+1) not in nodes:
                    moveTo = loopCordsX[(moveTo[0], moveTo[1])]
                else:
                    moveTo = (moveTo[0], moveTo[1]+1)
            elif direction == "L":
                if (moveTo[0], moveTo[1]-1) not in nodes:
                    moveTo = loopCordsX[(moveTo[0], moveTo[1])]
                else:
                    moveTo = (moveTo[0], moveTo[1]-1)
            elif direction == "U":
                if (moveTo[0]-1, moveTo[1]) not in nodes:
                    moveTo = loopCordsY[(moveTo[0], moveTo[1])]
                else:
                    moveTo = (moveTo[0]-1, moveTo[1])
            else:
                if (moveTo[0]+1, moveTo[1]) not in nodes:
                    moveTo = loopCordsY[(moveTo[0], moveTo[1])]
                else:
                    moveTo = (moveTo[0]+1, moveTo[1])
            
            
            if nodes[moveTo].wall == True:
                break
            else:
                currentPos = moveTo

currentPos = (currentPos[0]+1, currentPos[1]+1) # convert to rows and columns starting from 1

total = 0
if direction == "R":
    total += 0
elif direction == "L":
    total += 2
elif direction == "U":
    total += 3
else:
    total += 1

total += ((1000 * currentPos[0]) + (4 * currentPos[1]))
print(total)