f = open("input.txt")
input = f.readlines()
f.close()

for x in range(len(input)):
    input[x] = input[x].strip()
    input[x] = input[x].split(" ")

# this sets up the instructions in the instruction queue
clock = 1
queue = {} # contains the instructions and the clock cycle they are meant to happen at
for instruc in input:
    if instruc[0] == "noop":
        clock += 1
    else:
        queue[clock+1] = int(instruc[1])
        clock += 2

# executes all the insturctions
clock = 1
register = 1
checkClock = 20 # the cycle number to check
total = 0
while len(queue) != 0:
    if clock == checkClock:
        total += (clock * register)
        checkClock += 40
    
    # executes an addx command
    if clock in queue:
        register += queue[clock]
        queue.pop(clock)
    
    clock += 1

print(total)
