prod_dict = {}

n = int(input())

for _ in range(n):
    merch, rate = input().split()
    rate = int(rate)

    P = 0
    N = 0

    value_input = [0, 0, 0, 1]  # I, P, N, T

    if rate >= 4:       # P
        P = 1
        value_input[1] = P
    elif rate <= 2:     # N
        N = 1
        value_input[2] = N

    value_input[0] = P - N

    if merch in prod_dict:
        value = prod_dict[merch]
        # prod_dict[merch] = list(map(lambda x, y: x + y, value, value_input))
        prod_dict[merch] = [x + y for x, y in zip(value, value_input)]

    else:
        prod_dict[merch] = value_input

prod_list = []

for key, value in prod_dict.items():
    prod_list.append([key, *value])

prod_list.sort(key=lambda x: (-x[1], -x[4], x[0]))

for i in prod_list:
    print(*i)


# print(prod_dict)


"""
I = P - N   индекс удовлетворенности = кол-во положительных - кол-во отрицательных

Определить для каждого товара:
- I
- кол-во P
- кол-во N
- Т (общее кол-во) = P + N

сортировка (-I, -T, merch)

print(merch, I, P, N, T)

8
apple 1
banana 2
orange 3
grape 4
apple 5
banana 4
orange 2
grape 1



"""

