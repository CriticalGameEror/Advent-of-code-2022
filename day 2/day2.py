f = open("input.txt")
input = f.readlines()
f.close()

for x in range(len(input)):
    input[x] = input[x].strip().split(" ")

# part 1
# score = 0
# for game in input:
#     me = ord(game[1]) % 87
#     enemy = ord(game[0]) % 64

#     if me == enemy:
#         score += me + 3
#     elif (me == 1 and enemy == 3) or (me == 2 and enemy == 1) or (me == 3 and enemy == 2):
#         score += me + 6 
#     else:
#         score += me

# part 2
score = 0
for game in input:
    # converts the letters to ASCII as to normalise both to the range 1 to 3
    me = ord(game[1]) % 87
    enemy = ord(game[0]) % 64

    if me == 1:
        if enemy - 1 == 0:
            score += 3
        else:
            score += (enemy - 1)
    elif me == 2:
        score += enemy + 3
    else:
        if enemy + 1 == 4:
            score += 1
        else:    
            score += enemy + 1
        score += 6
        
print(score)