with open("input.txt") as f:
    input = f.read().split()

class Node:
    # connected is a list (of len max 4) of the position of surrounding nodes in form [y,x]
    def __init__(self, value, connected, name, final=False) -> None:
        self.visited = False
        self.connected = connected
        self.final = final
        self.name = name
    
    def __repr__(self) -> str:
        return self.name

# this assigns the nodes
nodeList = {}
startPosition = [0,0]
for y in range(len(input)):
    for x in range(len(input[y])):
        connected = []
        if input[y][x] == "S":
            value = (ord("a") % 96)
            startPosition = [y, x]
        else:
            value = (ord(input[y][x]) % 96)

        for itemy in [-1,0,1]:
            for itemx in [-1,0,1]:
                if itemy == itemx or (itemy != 0 and itemx != 0):
                    continue
                if y+itemy == len(input) or x+itemx == len(input[y]) or y+itemy < 0 or x+itemx < 0:
                    continue
                if ord(input[itemy+y][itemx+x]) % 96 > value+1:
                    if input[itemy+y][itemx+x] == "E":
                        if ord("z") % 96 > value+1:
                            continue
                    elif not input[itemy+y][itemx+x] == "S":
                        continue
                connected.append([itemy+y, itemx+x])
        
        if input[y][x] == "E":
            nodeList[y, x] = Node(value, connected, input[y][x], True)
        else:
            nodeList[y, x] = Node(value, connected, input[y][x])

queue = []
for cords in nodeList[startPosition[0], startPosition[1]].connected:
    queue.append([cords, 0])
nodeList[startPosition[0], startPosition[1]].visited = True

while len(queue) != 0:
    item = queue.pop(0)
    currentPos = item[0]
    currentVal = item[1]+1
    if nodeList[currentPos[0], currentPos[1]].visited == True:
        continue

    currentNode = nodeList[currentPos[0], currentPos[1]]
    for connection in currentNode.connected:
        if nodeList[connection[0], connection[1]].visited != True:
            queue.append([connection, currentVal])
    currentNode.visited = True
    if currentNode.name == "E":
        print(currentVal)
        break