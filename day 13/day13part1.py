with open("input.txt") as f:
    input = f.read().split()

# takes the string list and converts it into a normal list
def findList(toFind, x=0):
    newList = []
    while x < len(toFind)-1:
        # if it descovers a sub-list
        if toFind[x] == "[":
            find = findList(toFind, x+1) # uses recursion to find the numbers inside the sub-list
            newList.append(find[0])
            x = find[1]
        # used for discovering the end to a sub-list
        elif toFind[x] == "]":
            x += 1
            return [newList, x]
        # moves on if it finds a comment        
        elif toFind[x] == ",":
            x += 1
        # found a number
        else:
            # this complies the number until it reaches a , [ or ] and as long as x is still less than the length-1
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
    # checks that the indexes of both lists hasn't gone over
    while index1 < len(list1) and index2 < len(list2):
        # if each type is an integer
        if type(list1[index1]) == int and type(list2[index2]) == int:
            # if they are the same then go to the next item
            if list2[index2] == list1[index1]:
                index1 += 1
                index2 += 1
            # otherwise it would be more or less than
            elif list1[index1] < list2[index2]:
                return "less"
            else:
                return "more"
        
        # this elif and the one below check if one isn't a list and then uses recursion to check them
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

        # this means both are lists so use recusion to get the integers bythemselves
        else:
            compared = compare(list1[index1], list2[index2])
            if compared == "more":
                return "more"
            elif compared == "less":
                return "less"
            elif compared == "equal":
                index1 += 1
                index2 += 1
    
    
    # if index1 has reached the end then it is less than list2
    if index1 == len(list1) and index2 != len(list2):
        return "less"
    # if index1 has not reached the end but index2 has then list1 is bigger
    elif index2 == len(list2) and index1 != len(list1):
        return "more"
    # otherwise the two lists are of equal length
    else:
        return "equal"

# this splits the packets up into list form
packets = []
for packet in input:
    packets.append(findList(packet[1:]))

# pairs each packet together
pairs = []
for pair in range(0, len(packets), 2):
    pairs.append([packets[pair], packets[pair+1]])

# finds if the packet pairs are in order
inOrder = []
for pair in pairs:
    compared = compare(pair[0], pair[1])
    if compared == "less" or compared == "equal":
        inOrder.append(True)
    else:
        inOrder.append(False)

# finds the sum of the indexes of the in-order pairs
total = 0
for x in range(len(inOrder)):
    if inOrder[x] == True:
        total += (x+1)
print(total)