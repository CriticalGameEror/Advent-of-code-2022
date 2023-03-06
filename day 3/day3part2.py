f = open("input.txt")
input = f.readlines()
f.close()

# splits the input into groups of 3
groups = []
for x in range(0, len(input), 3): 
    groups.append([input[x].strip(), input[x+1].strip(), input[x+2].strip()])

# assigns each priority value to each letter
alphabet = {}
for letter in range(65,91):
    alphabet[chr(letter)] = letter % 64 + 26
for letter in range(97, 123):
    alphabet[chr(letter)] = (letter % 96)

# finds the common item in each backpack for the group
badges = []
for group in groups:
    set1 = set(group[0])
    set2 = set(group[1])
    set3 = set(group[2])

    for common in list(set1.intersection(set2.intersection(set3))):
        badges.append(common)

# adds up the priorities
priority = 0
for badge in badges:
    priority += alphabet[badge]

print(priority)