import math
f = open("input.txt")
input = f.read().split()
f.close()

def findOperator(operator, oldNumber, operand):
    if operator == "*":
        return oldNumber * operand
    elif operator == "/":
        return oldNumber / operand
    elif operator == "+":
        return oldNumber + operand
    elif operator == "-":
        return oldNumber - operand


# operation in the form ["operator", number]
# test in the form [devidedNumb, passToTrue, passToFalse]
class Monkey:
    def __init__(self, items, operation, test) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.total = 0 # the amount of items inspected
    
    # returns who the item should be thrown to
    def throwItem(self, lcm):
        # gets the first item in the list
        currentItem = int(self.items.pop(0))
        if self.operation[1] == "old": # if it is multiplying by itself
            currentItem = findOperator(self.operation[0], currentItem, currentItem)
        else:
            currentItem = findOperator(self.operation[0], currentItem, int(self.operation[1]))
            
        self.total += 1
        currentItem = currentItem % lcm

        if currentItem % self.test[0] == 0:
            return [self.test[1], currentItem]
        else:
            return [self.test[2], currentItem]
    
    def addItem(self, item):
        self.items.append(item)

monkeyList = []

testNumbList = [] # contains all the test numbers

items = []
operation = []
test = []
for x in range(1, len(input)):
    if input[x] == "items:":
        index = x+1
        while input[index] != "Operation:":
            items.append(int(input[index].strip(",")))
            index += 1
    elif input[x] == "=":
        operation = [input[x+2], input[x+3]]
    elif input[x] == "by":
        test = [int(input[x+1]), int(input[x+7]), int(input[x+13])]
        testNumbList.append(int(input[x+1])) # adds a test number when it is seen
        monkeyList.append(Monkey(items, operation, test))
        items = []
        operation = []
        test = []

# calculates the LCM of all the numbers in testNumList
lcm = 1
for number in testNumbList:
    lcm = math.lcm(lcm, number)

currentMonkey = 0
for round in range(10000 * len(monkeyList)):
    while len(monkeyList[currentMonkey].items) != 0:
        dest = monkeyList[currentMonkey].throwItem(lcm)
        monkeyList[dest[0]].addItem(dest[1])
    
    currentMonkey = (currentMonkey+1) % len(monkeyList)

listOfTotals = []
for monkey in range(len(monkeyList)):
    listOfTotals.append(monkeyList[monkey].total)

listOfTotals.sort()
print(listOfTotals[-1] * listOfTotals[-2])