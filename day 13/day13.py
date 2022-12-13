with open("input.txt") as f:
    input = f.read().split()

def findList(toFind, x=0):
    newList = []
    while x < len(toFind):
        if toFind[x] == "[":
            find = findList(toFind, x+1)
            newList.append(find[0])
            x = find[1]
            continue
        elif toFind[x] == "]":
            return [newList, x+1]
        elif toFind[x] != ",":
            newList.append(int(toFind[x]))
        x += 1
    return [newList, x]

# more means that the index1 is more than index2 which is invalid
# equal means index1 is the same as index2
# less means that index1 is less than index2 which is valid

# issue: if list 1 is one length and list 2 is multi length. If two elements are equal, it says it is more when it is not
def compare(list1, list2):
    index1 = 0
    index2 = 0
    while index1 < len(list1) and index2 < len(list2):
        # if each type is an integer
        if type(list1[index1]) == int and type(list2[index2]) == int:
            if list2[index2] == list1[index1]:
                index1 += 1
                index2 += 1
            elif list1[index1] < list2[index2]:
                return "less"
            else:
                return "more"
        
        elif type(list1[index1]) == int and type(list2[index2]) != int:
            compared = compare([list1[index1]], list2[index2])
            if compared == "more":
                return "more"
            elif compared == "less":
                return "less"
            elif compared == "equal":
                index1 += 1
                index2 += 1
        
        elif type(list1[index1]) != int and type(list2[index2]) == int:
            compared = compare(list1[index1], [list2[index2]])
            if compared == "more":
                return "more"
            elif compared == "less":
                return "less"
            elif compared == "equal":
                index1 += 1
                index2 += 1

        else:
            compared = compare(list1[index1], list2[index2])
            if compared == "more":
                return "more"
            elif compared == "less":
                return "less"
            elif compared == "equal":
                index1 += 1
                index2 += 1
    
    if index1 == len(list1) and index2 != len(list2):
        return "less"
    elif index2 == len(list2) and index1 != len(list1):
        return "more"
    else:
        return "equal"

packets = []
for packet in input:
    packets.append(findList(packet[1:])[0])

pairs = []
for pair in range(0, len(packets), 2):
    pairs.append([packets[pair], packets[pair+1]])

# inOrder = []
# for pair in pairs:
#     compared = compare(pair[0], pair[1])
#     if compared == "less" or compared == "equal":
#         inOrder.append(True)
#     else:
#         inOrder.append(False)

print(compare([[7,7],6,[],5,[3,3]], [5,[4,6]]))

# total = 0
# for x in range(len(inOrder)):
#     if inOrder[x] == True:
#         total += (x+1)
# print(total)

# True
# True
# False
# True
# False
# True
# False
# False