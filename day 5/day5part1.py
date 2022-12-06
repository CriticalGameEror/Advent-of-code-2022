class Stack:
    def __init__(self, items) -> None:
        self.stackList = items
        self.pointer = 0
    
    def addItem(self, item):
        self.pointer += 1
        self.stackList.append(item)
    def pop(self):
        self.pointer -= 1
        print(self.stackList, self.pointer)
        return self.stackList.pop(self.pointer+1)

f = open("input.txt")
input = f.readlines()
f.close()

for x in range(len(input)):
    input[x] = input[x].strip("\n")

# makes stacks
stackList = []
index = 0
for x in range(1, len(input[0])-1, 4):
    stackList.append(Stack([input[2][x], input[1][x], input[0][x]]))

# removes everything from the input appart from the instructions
thing = " "
while thing != "":
    thing = input.pop(0)

instrucs = []
for x in range(len(input)):
    input[x] = input[x].split(" ")
    instrucs.append([int(input[x][1]), int(input[x][3]), int(input[x][5])])

for instruc in instrucs:
    for x in range(instruc[0]):
        stackList[2].addItem(stackList[instruc[1]-1].pop())



