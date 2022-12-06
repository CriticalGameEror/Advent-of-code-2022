f = open("input.txt")
input = f.read()
f.close()

# part 1
def find_start(input):
    for letter in range(len(input)):
        if len(set(input[letter:letter+4])) == 4:
            return letter+4

# part 2
def find_message(input):
    for letter in range(len(input)):
        if len(set(input[letter:letter+14])) == 14:
            return letter+14


print(find_start(input))
print(find_message(input))