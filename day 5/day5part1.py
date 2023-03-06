f = open("input.txt")
input = f.readlines()
f.close()

for x in range(len(input)):
    input[x] = input[x].strip("\n")

# make each stack
stack_parse = []
instrucs = []
for item in input:
    if item.count("move") == 1: # detects the instrucstions
        instrucs.append(item)
    elif item.count("[") >= 1: # detects a stack
        stack_parse.append(item)

# puts each of the stacks into an array
stacks = []
loop_times = ((len(stack_parse[0])-1) // 4) + 1
item = -3
ref = 0 # the stack number
for y in range(loop_times):
    item += 4
    stacks.append([])
    for x in range(-1, -(len(stack_parse)+1), -1):
        if stack_parse[x][item] != " ":
            stacks[ref].append(stack_parse[x][item])
    ref += 1

# splits the instrucstions up
for x in range(len(instrucs)):
    instrucs[x] = instrucs[x].split(" ")
    instrucs[x].remove("move")
    instrucs[x].remove("from")
    instrucs[x].remove("to")

for instruc in instrucs:
    while len(stacks) < int(instruc[2])-1:
        stacks.append([])
    for item in range(int(instruc[0])):
        stacks[int(instruc[2])-1].append(stacks[int(instruc[1])-1].pop(-1))

answer = []
for item in stacks:
    answer.append(item[-1])

print("".join(answer))

