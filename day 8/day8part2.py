f = open("input.txt")
input = f.read().split()
f.close()

def checkX(input, x, y, value):
    total1 = 0
    for x_loop in range(x+1, len(input[y])):
        if input[y][x_loop] < value:
            total1 += 1
        elif input[y][x_loop] >= value:
            total1 += 1
            break
    total2 = 0
    for x_loop in range(x-1, -1, -1):
        if input[y][x_loop] < value:
            total2 += 1
        else:
            total2 += 1
            break
    return total1 * total2

def checkY(input, x, y, value):
    total1 = 0
    for y_loop in range(y+1, len(input)):
        if input[y_loop][x] < value:
            total1 += 1
        else:
            total1 += 1
            break
    total2 = 0
    for y_loop in range(y-1, -1, -1):
        if input[y_loop][x] < value:
            total2 += 1
        else:
            total2 += 1
            break
    return total1 * total2

count = []
for y in range(1, len(input)-1):
    for x in range(1, len(input[y])-1):
        count.append(checkX(input, x, y, input[y][x]) * checkY(input, x, y, input[y][x]))

count.sort()

print(count[-1])