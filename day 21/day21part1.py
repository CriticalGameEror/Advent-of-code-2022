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
    if type(monkeys[currentMonkey]) == Yell:
        return monkeys[currentMonkey].number
    else:
        calc = monkeys[currentMonkey].calc
        return monkeys[currentMonkey].add(findMoneky(calc[0]), findMoneky(calc[2]))

print(int(findMoneky("root")))