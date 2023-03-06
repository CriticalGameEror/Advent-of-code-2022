with open("input.txt") as f:
    input = f.read().split()

def findNumber(number):
    decimal = 0 # the number being calculated
    index = len(number)-1 # the unit position, (2 for example is 5 ** 2)
    for x in range(len(number)):
        unit = (5 ** index)
        if number[x] == "=":
            decimal += (unit * -2)
        elif number[x] == "-":
            decimal += (unit * -1)
        else:
            decimal += (unit * int(number[x]))
        
        index -= 1 # goes to the next unit position
    return decimal

def recision(target, currentNumb, currentSnafu, index, action):
    # if the current index is too big
    if (5 ** index) > abs(target):
        return None
    
    # add the action to the number and then the snafu number
    if action == "2":
        currentNumb += ((5 ** index) * 2)
    elif action == "1":
        currentNumb += ((5 ** index) * 1)
    elif action == "-":
        currentNumb += ((5 ** index) * -1)
    elif action == "=":
        currentNumb += ((5 ** index) * -2)
    currentSnafu = action + currentSnafu

    # has reached the target number
    if currentNumb == target:
        return currentSnafu

    one = recision(target, currentNumb, currentSnafu, index+1, "2")
    if one != None:
        return one
    two = recision(target, currentNumb, currentSnafu, index+1, "1")
    if two != None:
        return two
    three = recision(target, currentNumb, currentSnafu, index+1, "0")
    if three != None:
        return three
    four =  recision(target, currentNumb, currentSnafu, index+1, "-")
    if four != None:
        return four
    five = recision(target, currentNumb, currentSnafu, index+1, "=")
    if five != None:
        return five

    return None

def findSnafu(number):
    one = recision(number, 0, "", 0, "2")
    if one != None:
        return one
    print("hello")
    two = recision(number, 0, "", 0, "1")
    if two != None:
        return two
    print("hello")
    three = recision(number, 0, "", 0, "0")
    if three != None:
        return three
    print("hello")
    four =  recision(number, 0, "", 0, "-")
    if four != None:
        return four
    print("hello")
    five = recision(number, 0, "", 0, "=")
    if five != None:
        return five


total = 0
for number in input:
    total += findNumber(number)

print(total)

print(findSnafu(total))
# hello    

