with open("input.txt") as f:
    input = f.read().split()

class Monkey:
    def __init__(self, name) -> None:
        self.name = name

class Yell(Monkey):
    def __init__(self, name, number) -> None:
        super().__init__(name)
        self.number = number

class Wait(Monkey):
    def __init__(self, name, first, second, operator) -> None:
        super().__init__(name)
        self.calc = [first, operator, second]
    
    def add(self, first, second):
        match (self.calc[1]):
            case "+":
                return first + second
            case "-":
                return first - second
            case "*":
                return first * second
            case "/":
                return first / second

class Human(Monkey):
    def __init__(self, name) -> None:
        self.name = name

    def setNumber(self, number):
        self.number = number

class Root(Monkey):
    def __init__(self, name, first, second) -> None:
        super().__init__(name)
        self.first = first
        self.second = second

    def equal(self, first, second):
        return abs(first - second)

monkeys = {}

newMonkey = True
monkeyName = ""
calc = []
number = 0

x = 0
while x != len(input):
    if newMonkey:
        newMonkey = False
        monkeyName = input[x].strip(":")
    elif monkeyName == "humn":
        monkeys[monkeyName] = Human(monkeyName)
        newMonkey = True
    elif monkeyName == "root":
        monkeys[monkeyName] = Root(monkeyName, input[x], input[x+2])
        x += 2
        newMonkey = True
    else:
        try:
            number = int(input[x])
            monkeys[monkeyName] = Yell(monkeyName, number)
            newMonkey = True
        except:
            calc = [input[x], input[x+1], input[x+2]]
            monkeys[monkeyName] = Wait(monkeyName, calc[0], calc[2], calc[1])
            x += 2
            newMonkey = True
    x += 1

def findMoneky(currentMonkey):
    if type(monkeys[currentMonkey]) == Yell or type(monkeys[currentMonkey]) == Human:
        return monkeys[currentMonkey].number
    elif type(monkeys[currentMonkey]) == Root:
        return monkeys[currentMonkey].equal(findMoneky(monkeys[currentMonkey].first), findMoneky(monkeys[currentMonkey].second))
    else:
        calc = monkeys[currentMonkey].calc
        return monkeys[currentMonkey].add(findMoneky(calc[0]), findMoneky(calc[2]))

'''
A manual approach. Scan a range of numbers. See the lowest difference that was achieved from the two root values and the humn value this occured at. 
Ammend the range search to be more specific to the lowest value found. 
Continue to change the range until it is specific enough to loop through each number in increments of 1
Once the difference is zero, the correct value to shout has been found
'''


highest = [None, None] # for testing purposes, to see the highest difference and the x value it occured at
for x in range(3219579390000, 3219579397000, 1): 
    monkeys["humn"].setNumber(x)
    match = findMoneky("root")
    print(match, x)
    if int(match) == 0:
        print(x)
        exit()
    if highest[0] == None:
        highest[0] = match
        highest[1] = x
    elif match < highest[0]:
        highest[0] = match
        highest[1] = x

print(highest)