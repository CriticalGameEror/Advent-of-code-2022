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
register = 1 # position of the sprite
screen = []
while clock != 241: # loops up to the 240th cycle
    render = (clock-1) % 40 # loops the renderer around once each line has been rendered
    # detects if it should render a pixel from the sprite's current position
    if (render == register) or (render == register+1) or (render == register-1):
        screen.append("#")
    else:
        screen.append(".")
    
    if clock in queue:
        register += queue[clock]
        queue.pop(clock)
    
    clock += 1

# prints the screen
for pixel in range(0, len(screen), 40):
    print("".join(screen[pixel:pixel+40]))



