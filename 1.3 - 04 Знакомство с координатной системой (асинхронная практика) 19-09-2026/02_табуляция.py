import math

title = "Число\tКвадратный корень\tКубический корень"
print(title)
print('=' * (len(title) + 2))

for i in range(2, 10):
    k = math.sqrt(i)
    k3 = i ** (1/3)
    print(f'{i:>5}\t{k:17.4f}\t{k3:.4f}')
