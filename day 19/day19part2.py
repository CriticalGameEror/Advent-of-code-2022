# help from: https://www.reddit.com/r/adventofcode/comments/zpihwi/comment/j0tls7a/?utm_source=share&utm_medium=web2x&context=3
with open("input.txt") as f:
    input = f.read().split()

# BFS during each min, branches to make every type of bot out of the 4

maxGeode = 0
def findHighestGeode(materials, robots, blueprint, goalRobot, time=32):
    global maxGeode
    # checks if the goal robot is possible to make
    if goalRobot == "obsidian" and robots["clay"] == 0:
        return
    elif goalRobot == "geode" and robots["obsidian"] == 0:
        return
    
    goalReached = False
    while time != 0:
        # checks to see if the goal robot can be bought
        bought = []
        if goalRobot == "ore":
            if materials["ore"] >= blueprint["ore"]["ore"]:
                materials["ore"] -= blueprint["ore"]["ore"]
                bought.append("ore")
                goalReached = True
        elif goalRobot == "clay":
            if materials["ore"] >= blueprint["clay"]["ore"]:
                materials["ore"] -= blueprint["clay"]["ore"]
                bought.append("clay")
                goalReached = True
        elif goalRobot == "obsidian":
            if materials["ore"] >= blueprint["obsidian"]["ore"] and materials["clay"] >= blueprint["obsidian"]["clay"]:
                materials["ore"] -= blueprint["obsidian"]["ore"]
                materials["clay"] -= blueprint["obsidian"]["clay"]
                bought.append("obsidian")
                goalReached = True
        elif goalRobot == "geode":
            if materials["ore"] >= blueprint["geode"]["ore"] and materials["obsidian"] >= blueprint["geode"]["obsidian"]:
                materials["ore"] -= blueprint["geode"]["ore"]
                materials["obsidian"] -= blueprint["geode"]["obsidian"]
                bought.append("geode")
                goalReached = True
        
        # generate the materials
        for material in ["ore", "clay", "obsidian", "geode"]:
            materials[material] += robots[material]
        
        # constructs any bought robots
        for robot in bought:
            robots[robot] += 1

        time -= 1

        # starts another loop if the goal is found
        if goalReached:
            if int((robots["geode"] * time) + materials["geode"] + ((time-1)*(time/2))) <= maxGeode: # if its not possible to generate enough geodes in the best possible scenario
                return
            else:
                if robots["ore"] < blueprint["ore"]["ore"] or robots["ore"] < blueprint["clay"]["ore"] or robots["ore"] < blueprint["obsidian"]["ore"] or robots["ore"] < blueprint["geode"]["ore"]:
                    findHighestGeode(materials.copy(), robots.copy(), blueprint.copy(), "ore", time)
                if robots["clay"] < blueprint["obsidian"]["clay"]:
                    findHighestGeode(materials.copy(), robots.copy(), blueprint.copy(), "clay", time)
                if robots["obsidian"] < blueprint["geode"]["obsidian"]:
                    findHighestGeode(materials.copy(), robots.copy(), blueprint.copy(), "obsidian", time)
                findHighestGeode(materials.copy(), robots.copy(), blueprint.copy(), "geode", time)
            return
    
    if materials["geode"] > maxGeode:
        maxGeode = materials["geode"]
    return
        

materials = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0} # the materials that are currently collected
robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0} # the robots currently constructed
blueprint = {} # how much each robot costs
bluePrintNumb = 1
total = 1
for x in range(0, len(input), 32):
    if bluePrintNumb == 4:
        break

    # assigns blueprint values
    blueprint["ore"] = {input[x+7].strip("."): int(input[x+6])}
    blueprint["clay"] = {input[x+13].strip("."): int(input[x+12])}
    blueprint["obsidian"] = {input[x+19].strip("."): int(input[x+18]), input[x+22].strip("."): int(input[x+21])}
    blueprint["geode"] = {input[x+28].strip("."): int(input[x+27]), input[x+31].strip("."): int(input[x+30])}

    findHighestGeode(materials.copy(), robots.copy(), blueprint.copy(), "ore")
    findHighestGeode(materials.copy(), robots.copy(), blueprint.copy(), "clay")
    total *= maxGeode
    print(maxGeode)
    print(bluePrintNumb)

    maxGeode = 0
    bluePrintNumb += 1

print(total)