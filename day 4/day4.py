f = open("input.txt")
input = f.readlines()
f.close()

for x in range(len(input)):
    input[x] = input[x].strip().split(",")

    input[x][0] = input[x][0].split("-")
    input[x][1] = input[x][1].split("-")

# part 1
# total = 0
# for pair in input:
#     set1 = set(x for x in range(int(pair[0][0]), int(pair[0][1])+1))
#     set2 = set(x for x in range(int(pair[1][0]), int(pair[1][1])+1))

#     intersect = list(set1.intersection(set2))
#     if intersect == []:
#         continue
#     if intersect == list(set1) or intersect == list(set2):
#         total += 1

# part 2
total = 0
for pair in input:
    set1 = set(x for x in range(int(pair[0][0]), int(pair[0][1])+1))
    set2 = set(x for x in range(int(pair[1][0]), int(pair[1][1])+1))

    intersect = list(set1.intersection(set2))
    if intersect == []:
        continue
    total += 1

print(total)