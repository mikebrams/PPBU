pos = input()

letters = 'abcdefgh'

pos_new =  letters.index(pos[0]) + 1, int(pos[1])

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2) ,(-1, 2), (-1, -2)]

counter = 0

for i in range(8):
    if   0 < moves[i][0] + pos_new[0] <= 8 and 0 < moves[i][1] + pos_new[1] <= 8:
        counter += 1

print(counter)