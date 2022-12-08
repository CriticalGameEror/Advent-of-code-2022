f = open("input.txt")
input = f.read().split()
f.close()

def checkX(input, x, y, value):
    visible = False
    for x_loop in range(x+1, len(input[y])):
        if input[y][x_loop] < value:
            visible = True
        elif input[y][x_loop] >= value:
            visible = False
            break
    if visible:
        return True
    for x_loop in range(0, x):
        if input[y][x_loop] < value:
            visible = True
        else:
            visible = False
            break
    return visible

def checkY(input, x, y, value):
    visible = False
    for y_loop in range(y+1, len(input)):
        if input[y_loop][x] < value:
            visible = True
        else:
            visible = False
            break
    if visible:
        return True
    for y_loop in range(0, y):
        if input[y_loop][x] < value:
            visible = True
        else:
            visible = False
            break
    return visible

count = 0
for y in range(1, len(input)-1):
    for x in range(1, len(input[y])-1):
        if checkX(input, x, y, input[y][x]) or checkY(input, x, y, input[y][x]):
            count += 1

count += (len(input[0]) * 2) + ((len(input)-2) * 2)
print(count)