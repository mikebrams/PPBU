min_noise = 121
first_measure = 1
quantity = 1

for i in range(1, int(input())+1):
    noise = int(input())

    if noise == min_noise:
        quantity += 1

    if noise < min_noise:
        min_noise = noise
        first_measure = i
        quantity = 0
        quantity += 1

print(min_noise, first_measure, quantity)

"""
3
120
120
0

0 3 1
"""