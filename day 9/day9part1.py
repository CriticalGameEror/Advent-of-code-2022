import math
f = open("input.txt")
input = f.read().split()
f.close()

visited = []
head = [0,0]
tail = [0,0]

visited.append(tail.copy()) # appends the starting position

# checks if the tail is agacent to the head
def checkAgacent():
    if math.fabs(head[0] - tail[0]) > 1 or math.fabs(head[1] - tail[1]) > 1:
        return False
    return True
    
def moveTail():
    # moves the tail if head is on the same column
    if head[0] == tail[0]:
        if head[1] > tail[1]: # moves up
            tail[1] += 1
        else:
            tail[1] -= 1 # moves down
    # moves the tail if the head is on the same role
    elif head[1] == tail[1]:
        if head[0] > tail[0]: # moves right
            tail[0] += 1
        else:
            tail[0] -= 1 # moves left
    # moves the tail diagonally if the head is further to the right
    elif head[0] > tail[0]:
        if head[1] > tail[1]: # moves tail up
            tail[1] += 1
        else:
            tail[1] -= 1 # moves tail down
        tail[0] += 1
    # moves the tail diagonally iff the head is further to the left
    elif head[0] < tail[0]:
        if head[1] > tail[1]:
            tail[1] += 1 # moves tail up
        else:
            tail[1] -= 1 # moves tail down
        tail[0] -= 1    
    # adds the tail to the list of visited areas if its not already been visited
    if tail not in visited:
        visited.append(tail.copy())

# loops through each instruction
for instruc in range(0, len(input), 2):
    if input[instruc] == "R":
        for loop in range(int(input[instruc+1])):
            head[0] += 1
            if not checkAgacent():
                moveTail()
    elif input[instruc] == "U":
        for loop in range(int(input[instruc+1])):
            head[1] += 1
            if not checkAgacent():
                moveTail()
    elif input[instruc] == "L":
        for loop in range(int(input[instruc+1])):
            head[0] -= 1
            if not checkAgacent():
                moveTail()
    elif input[instruc] == "D":
        for loop in range(int(input[instruc+1])):
            head[1] -= 1
            if not checkAgacent():
                moveTail()

print(len(visited))