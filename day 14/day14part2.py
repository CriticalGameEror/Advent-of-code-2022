with open("input.txt") as f:
    input = f.readlines()

for x in range(len(input)):
    input[x] = input[x].strip()
    input[x] = input[x].split("->")
    for y in range(len(input[x])):
        input[x][y] = input[x][y].split(",")
    
locations = {} # [x,y] - key
boundaries = [10000000000, 0, 0] # lowest x, highest x, highest y
for rockform in input:
    for rock in range(0, len(rockform)-1):
        x = int(rockform[rock][0])
        y = int(rockform[rock][1])
        while (x != int(rockform[rock+1][0])) or (y != int(rockform[rock+1][1])):
            
            if x < boundaries[0]:
                boundaries[0] = x
            if x > boundaries[1]:
                boundaries[1] = x
            if y > boundaries[2]:
                boundaries[2] = y

            if int(rockform[rock+1][0]) < boundaries[0]:
                boundaries[0] = int(rockform[rock+1][0])
            if int(rockform[rock+1][0]) > boundaries[1]:
                boundaries[1] = int(rockform[rock+1][0])
            if int(rockform[rock+1][1]) > boundaries[2]:
                boundaries[2] = int(rockform[rock+1][1])

            locations[x,y] = "rock"
            if x != int(rockform[rock+1][0]):
                if x < int(rockform[rock+1][0]):
                    x += 1
                else:
                    x -= 1
            else:
                if y < int(rockform[rock+1][1]):
                    y += 1
                else:
                    y -= 1
        locations[x,y] = "rock"

boundaries[2] += 2

total = 0
currentLocation = [500,0]
while True:
    if (currentLocation[1] == boundaries[2]-1):
        locations[currentLocation[0], currentLocation[1]] = "sand"
        currentLocation = [500,0]
        total += 1
    if (currentLocation[0], currentLocation[1]+1) not in locations:
        currentLocation = [currentLocation[0], currentLocation[1]+1]
    elif (currentLocation[0]-1, currentLocation[1]+1) not in locations:
        currentLocation = [currentLocation[0]-1, currentLocation[1]+1]
    elif (currentLocation[0]+1, currentLocation[1]+1) not in locations:
        currentLocation = [currentLocation[0]+1, currentLocation[1]+1]
    else:
        if (currentLocation[0] == 500 and currentLocation[1] == 0):
            total += 1
            break
        locations[currentLocation[0], currentLocation[1]] = "sand"
        currentLocation = [500,0]
        total += 1

print(total)