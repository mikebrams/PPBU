from itertools import product

a = product('01', repeat=4)

for i, j in enumerate(a, start=1):
    print(f'{i:3}:   {j}')