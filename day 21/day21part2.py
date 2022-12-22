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
        if first == second:
            return True
        else:
            return False

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

match = False
number = 0
while match == False:
    monkeys["humn"].setNumber(number)
    match = findMoneky("root")
    print(number)
    number += 1