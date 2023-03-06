f = open("input.txt")
input = f.readlines()
f.close()

# splits up the compartment of each backpack
for x in range(len(input)): 
    input[x] = input[x].strip()
    half = int(len(input[x])/2)
    input[x] = [input[x][:half], input[x][half:]]

# finds the common characters of each compartment in each backpack
dupes = []
for backpack in input:
    set1 = set(backpack[0])
    set2 = set(backpack[1])

    for dupe in list(set1.intersection(set2)):
        dupes.append(dupe)

# assigns the priority values to the letters
alphabet = {}
for letter in range(65,91):
    alphabet[chr(letter)] = letter % 64 + 26
for letter in range(97, 123):
    alphabet[chr(letter)] = (letter % 96)

# adds up the priorities
priority = 0
for dupe in dupes:
    priority += alphabet[dupe]

print(priority)