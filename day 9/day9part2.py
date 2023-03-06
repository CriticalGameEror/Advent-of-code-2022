f = open("input.txt")
input = f.read().split()
f.close()

class Chain():
    def __init__(self, front, back) -> None:
        self.front = front
        self.back = back
        self.loc = [0,0]


visited = []
head = Chain(None, None)
current = head
# appends the chain of knots to the head
for x in range(9):
    current.back = Chain(current, None)
    current = current.back

visited.append(head.loc.copy()) # appends the starting position

# checks if the parent and current knots are touching
def checkAgacent(parent, current):
    if abs(parent.loc[0] - current.loc[0]) > 1 or abs(parent.loc[1] - current.loc[1]) > 1:
        return False
    return True
    
def moveTails():
    previous = head
    current = head.back
    # see part 1 for comments as it is a similar method
    while True:
        if not checkAgacent(previous, current):
            if previous.loc[0] == current.loc[0]:
                if previous.loc[1] > current.loc[1]:
                    current.loc[1] += 1
                else:
                    current.loc[1] -= 1
            elif previous.loc[1] == current.loc[1]:
                if previous.loc[0] > current.loc[0]:
                    current.loc[0] += 1
                else:
                    current.loc[0] -= 1
            elif previous.loc[0] > current.loc[0]:
                if previous.loc[1] > current.loc[1]:
                    current.loc[1] += 1
                else:
                    current.loc[1] -= 1
                current.loc[0] += 1
            elif previous.loc[0] < current.loc[0]:
                if previous.loc[1] > current.loc[1]:
                    current.loc[1] += 1
                else:
                    current.loc[1] -= 1
                current.loc[0] -= 1
        # if its the last knot then break
        if current.back == None:
            break
        # otherwise the previous and current knots are set
        previous = current
        current = current.back
    # adds the location of the last knot to the visited list if the location it is at has not already been visited
    if current.loc not in visited:
        visited.append(current.loc.copy())

# loops through each instruction
for instruc in range(0, len(input), 2):
    if input[instruc] == "R":
        for loop in range(int(input[instruc+1])):
            head.loc[0] += 1
            moveTails()
    elif input[instruc] == "U":
        for loop in range(int(input[instruc+1])):
            head.loc[1] += 1
            moveTails()
    elif input[instruc] == "L":
        for loop in range(int(input[instruc+1])):
            head.loc[0] -= 1
            moveTails()
    elif input[instruc] == "D":
        for loop in range(int(input[instruc+1])):
            head.loc[1] -= 1
            moveTails()

print(len(visited))