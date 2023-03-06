with open("input.txt") as f:
    input = f.read().split()

def findList(toFind, x=0):
    newList = []
    while x < len(toFind)-1:
        if toFind[x] == "[":
            find = findList(toFind, x+1)
            newList.append(find[0])
            x = find[1]
        elif toFind[x] == "]":
            x += 1
            return [newList, x]
        elif toFind[x] == ",":
            x += 1
        else:
            number = ""
            while toFind[x] != "," and toFind[x] != "[" and toFind[x] != "]" and x < len(toFind)-1:
                number += toFind[x]
                x += 1
            newList.append(int(number))
    return newList


# more means that the index1 is more than index2 which is invalid
# equal means index1 is the same as index2
# less means that index1 is less than index2 which is valid

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
    packets.append(findList(packet[1:]))

packets.append([[2]])
packets.append([[6]])

hit = True
while hit == True:
    hit = False
    for x in range(0,len(packets)-1):
        compared = compare(packets[x], packets[x+1])
        if compared == "more":
            packets[x], packets[x+1] = packets[x+1], packets[x]
            hit = True

total = 1
for x in range(len(packets)):
    if packets[x] == [[2]] or packets[x] == [[6]]:
        total *= (x+1)
print(total)