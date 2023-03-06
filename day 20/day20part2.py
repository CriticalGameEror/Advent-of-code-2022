with open("input.txt") as f:
    input = f.read().split()

class Item:
    def __init__(self, index, number) -> None:
        self.index = index
        self.number = number
    
    def __repr__(self) -> str:
        return str(self.number)

seq = []
for number in range(len(input)):
    seq.append(Item(number, int(input[number]) * 811589153))

for mix in range(10): # mixes the numbers 10 times
    seqIndex = 0
    while seqIndex != len(input):
        for currentIndex in range(len(seq)):
            if seq[currentIndex].index == seqIndex:
                number = seq.pop(currentIndex)
                index = (currentIndex + number.number) % len(seq)
                if index <= 0:
                    index = len(seq) + (currentIndex + number.number)
                seq = seq[:index] + [number] + seq[index:]

                seqIndex += 1
                break

for number in range(len(seq)):
    if seq[number].number == 0:
        startingPoint = number

total = 0
for x in range(1000, 3001, 1000):
   total += seq[(x+startingPoint)%len(seq)].number
print(total)