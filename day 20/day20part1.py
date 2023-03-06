with open("input.txt") as f:
    input = f.read().split()

# a class for each item in the main array
class Item:
    def __init__(self, index, number) -> None:
        self.index = index
        self.number = number
    
    def __repr__(self) -> str:
        return str(self.number)

# appends each item to the seq array, giving their original index (order of processing)
seq = []
for number in range(len(input)):
    seq.append(Item(number, int(input[number])))

# loops through until each index has been visited
seqIndex = 0
while seqIndex != len(input):
    for currentIndex in range(len(seq)):
        if seq[currentIndex].index == seqIndex: # if the item found is the next item that needs processing
            number = seq.pop(currentIndex) # remove the number that needs moving from the sequence
            index = (currentIndex + number.number) % len(seq) # find the new index position of the number
            if index <= 0: # if the index is less than 0
                index = len(seq) + (currentIndex + number.number) # find the new position of the index at the end of the array
            seq = seq[:index] + [number] + seq[index:] # adds the moved number back into the array at the correct position

            seqIndex += 1 # as to find the next index that needs to be moved
            break

# used to find where 0 is in the final seq
for number in range(len(seq)):
    if seq[number].number == 0:
        startingPoint = number

# finds the sum of the 1000th, 2000th and 3000th number
total = 0
for x in range(1000, 3001, 1000):
   total += seq[(x+startingPoint)%len(seq)].number
print(total)