import copy

a = 100
b = 100

print(id(a), id(b))

num = [1, 2, [3, 4]]

# nn = num[:]
# nn = num.copy()

nn = copy.deepcopy(num) # глубокое копирование

nn[1] = 22
nn[2][1] = 444

print(num)
print(nn)


num.append([100])     # O(1) константная сложность
print(num)
num.insert(0, 300)  # O(n) линейная сложность
print(num)

# Python выделяет сплошную адресацию для элементов списка !!!!!

num.extend([1, 2])
print(num)
