import sys
from itertools import count

"""
1. Определить минимальный 3-х значный элемент, заканчивающийся на 17

117
500
600
700
-1000
-1200
-1500
10
20
30
"""

data = list(map(int, sys.stdin.read().split()))

M = min([i for i in data if 100 <= i <= 999 and i % 100 == 17])

count_triple = 0
min_product = 0
max_spread = 0


# while True:

    # M = min([i for i in data if 100 <= i <= 999 and i % 100 == 17])

for i in range(len(data) - 2):
    triple = data[i:i + 3]
    if all(x > 0 for x in triple) or all(x < 0 for x in triple):
        low = min(triple)
        high = max(triple)
        product = low * high
        spread = high - low
        if product > M ** 2:
            count_triple += 1
            if min_product == 0 or product < min_product:
                min_product = product
            if spread > max_spread:
                max_spread = spread

print(count_triple, min_product, max_spread)
sys.exit()



# print(sys.version)
#
# print("Ожидание ввода...")
# for i, line in enumerate(sys.stdin, 1):
#     sys.stdout.write(f"{i}: {line}")

