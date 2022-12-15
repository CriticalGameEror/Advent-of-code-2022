with open("input.txt") as f:
    input = f.read().split()

class Sensor:
    def __init__(self, location, beaconLoc) -> None: # location in the form [x,y]
        self.location = location
        self.beacon = beaconLoc
        self.distance = abs(beaconLoc[0] - location[0]) + abs(beaconLoc[1] - location[1])

sensors = []
highestX = 0
highestY = 0
highestDist = 0

for x in range(0, len(input), 10):
    cordX = int(input[x+2].strip("x=,"))
    cordY = int(input[x+3].strip("y=:"))
    beaconX = int(input[x+8].strip("x=,"))
    beaconY = int(input[x+9].strip("y="))
    if cordX > highestX:
        highestX = cordX
    if beaconX > highestX:
        highestX = beaconX
    if cordY > highestY:
        highestY = cordY
    if beaconY > highestY:
        highestY = beaconY
    sensors.append(Sensor([cordX, cordY], [beaconX, beaconY]))

for sensor in sensors:
    if sensor.distance > highestDist:
        highestDist = sensor.distance

def findBeacon():
    for x in range(0, 4000001):
        for y in range(0, 4000001):
            print(x,y)
            toBreak = False
            cords = []
            for sensor in sensors:
                if abs(x - sensor.location[0]) + abs(y - sensor.location[1]) > sensor.distance:
                    cords = [x, y]
                    toBreak = True
                else:
                    toBreak = False
                    break
            if toBreak:
                return cords


loc = findBeacon()
print((loc[0]*4000000) + loc[1])