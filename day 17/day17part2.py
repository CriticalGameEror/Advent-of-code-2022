with open("input.txt") as f:
    input = f.read().strip()

class Rock:
    def moveDown(self):
        for loc in range(len(self.position)):
            self.position[loc][1] -= 1 
    
    def moveLeft(self):
        for loc in range(len(self.position)):
            self.position[loc][0] -= 1
    
    def moveRight(self):
        for loc in range(len(self.position)):
            self.position[loc][0] += 1

    def compareDown(self, positions):
        for loc in range(len(self.position)):
            if self.position[loc][1]-1 <= -1: # stops it from going into a wall
                return True
            if (self.position[loc][0], self.position[loc][1]-1) in positions:
                return True
        return False
    
    def compareLeft(self, positions):
        for loc in range(len(self.position)):
            if self.position[loc][0]-1 <= -1: # stops if from going into a wall
                return True
            if (self.position[loc][0]-1, self.position[loc][1]) in positions:
                return True
        return False

    def compareRight(self, positions):
        for loc in range(len(self.position)):
            if self.position[loc][0]+1 >= 7: # stops if from going into a wall
                return True
            if (self.position[loc][0]+1, self.position[loc][1]) in positions:
                return True
        return False
    
    def getHighestY(self):
        highest = -1
        for pos in self.position:
            if pos[1] > highest:
                highest = pos[1]
        return highest

class LineHor(Rock):
    def __init__(self, leftCord, yCord) -> None:
        self.position = [[leftCord, yCord], [leftCord+1, yCord], [leftCord+2, yCord], [leftCord+3, yCord]]

class Plus(Rock):
    def __init__(self, leftCord, yCord) -> None:
        self.position = [[leftCord,yCord+1], [leftCord+1, yCord+1], [leftCord+2, yCord+1], [leftCord+1, yCord], [leftCord+1, yCord+2]]

class L(Rock):
    def __init__(self, leftCord, yCord) -> None:
        self.position = [[leftCord, yCord], [leftCord+1, yCord], [leftCord+2, yCord], [leftCord+2, yCord+1], [leftCord+2, yCord+2]]

class LineVer(Rock):
    def __init__(self, leftCord, yCord) -> None:
        self.position = [[leftCord, yCord], [leftCord, yCord+1], [leftCord, yCord+2], [leftCord, yCord+3]]

class Square(Rock):
    def __init__(self, leftCord, yCord) -> None:
        self.position = [[leftCord, yCord], [leftCord, yCord+1], [leftCord+1, yCord], [leftCord+1, yCord+1]]

rocksDispense = "-+L|S"
positions = set() # the positions of all rocks
rockNumb = 1 # the number of rocks being generated
indexDispense = 0 # for the rock that needs to be chosed
indexMove = 0 # for dealing with the puzzle input
highestY = 0
startingPosition = None
while rockNumb != 100000000:
    # for finding the correct rock to generate
    rock = None
    match(rocksDispense[indexDispense]):
        case "-":
            rock = LineHor(2, highestY+3)
        case "+":
            rock = Plus(2, highestY+3)
        case "L":
            rock = L(2, highestY+3)
        case "|":
            rock = LineVer(2, highestY+3)
        case "S":
            rock = Square(2, highestY+3)
    if indexDispense+1 == len(rocksDispense):
        indexDispense = 0
    else:
        indexDispense += 1

    # to move the rock
    while True:
        # for moving the rock left or right
        move = True
        # moving the rock right
        if input[indexMove%len(input)] == ">":
            if rock.compareRight(positions) == True:
                move = False
            if move:
                rock.moveRight()
        # moving the rock left
        else:
            if rock.compareLeft(positions) == True:
                move = False
            if move:
                rock.moveLeft()

        indexMove += 1

        # for moving the rock down
        move = True
        if rock.compareDown(positions) == True:
            move = False
        if move:
            rock.moveDown()
        else:
            break
    
    # for finding the highest Y cord
    yCord = rock.getHighestY()+1
    if yCord > highestY:
        highestY = yCord

    for loc in rock.position:
        positions.add((loc[0], loc[1]))
    
    # check if it is a duplicate
    if startingPosition == None:
        startingPosition = [[],0]
        for loc in rock.position:
            startingPosition[0].append(loc[0]) # appends the x coords
        startingPosition[1] = (indexMove-1)%len(input)
        print(startingPosition)

    elif (indexMove-1)%len(input) == startingPosition[1]:
        print("hello")
        doBreak = False
        for loc in rock.position:
            if loc[0] not in startingPosition[0]:
                doBreak = True
        if not doBreak:
            print(rockNumb+1, highestY)
            exit()

    rockNumb += 1

print(highestY)