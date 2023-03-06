with open("input.txt") as f:
    input = f.read().split()

class Sensor:
    def __init__(self, location, beaconLoc) -> None: # location in the form [x,y]
        self.location = location
        self.beacon = beaconLoc
        self.distance = abs(beaconLoc[0] - location[0]) + abs(beaconLoc[1] - location[1])

sensors = []
highestX = 0
lowestX = 9999999999999999
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
    if cordX < lowestX:
        lowestX = cordX
    if beaconX < lowestX:
        lowestX = beaconX
    sensors.append(Sensor([cordX, cordY], [beaconX, beaconY]))

for sensor in sensors:
    if sensor.distance > highestDist:
        highestDist = sensor.distance

locations = []
def findEmpty(cordY):
    total = 0
    for x in range(lowestX-highestDist, (highestX+1)+highestDist):
        add = False
        for sensor in sensors:
            if abs(x - sensor.location[0]) + abs(cordY - sensor.location[1]) <= sensor.distance:
                if (x == sensor.beacon[0] and cordY == sensor.beacon[1]) or (x == sensor.location[0] and cordY == sensor.location[1]):
                    break
                else:
                    locations.append([x, cordY])
                    break
            else:
                continue

findEmpty(2000000)
print(len(locations))