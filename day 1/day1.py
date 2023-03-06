f = open("input.txt")
text = f.readlines()
f.close()

new_list = []
total = 0
for x in range(len(text)):
    if text[x] == "\n":
        new_list.append(total)
        total = 0
        continue
    total += int(text[x].strip())
new_list.append(total)

new_list.sort()

# part 1
#print(new_list[-1])

# part 2
#print(new_list[-1] + new_list[-2] + new_list[-3])