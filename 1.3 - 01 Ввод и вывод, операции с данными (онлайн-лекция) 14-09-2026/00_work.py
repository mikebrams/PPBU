print('00000000011111111112222222222')
print('12345678901234567890123456789')
print('Winter\tSpring\tSummer\tAutumn')
print('Зима\tВесна\tЛето\tОсень')


k1 = (1, 2, 3)
k2 = (4, 5, 6)
k3 = k1 + k2
print(k3)


k1 = (1, 2, 3)
k2 = k1 * 3
print(k2)

s2 = ['a', 'b', 'f']
s2[0] = 'l'
print(s2)

s1 = [1, 2, 3, 4]
s2 = s1.reverse()
print(s2) # Выведет: None
print(s1) # Выведет: [4, 3, 2, 1]

k1 = "Вихри снежные крутя"
k2 = tuple(k1)
print(k2)

pokupki = ['молоко', 'сметана', 'сыр', 'хлеб']
pokupki.clear()
print(pokupki)

s1 = ['Буря', 'мглою', 'небо', 'кроет']
print(max(s1))

url = "https://example.com/path/to/file.txt"
f = url.split("/")[-1]
print(f"Имя файла из URL: {f}")

path = 'C:\Python\Lesson\June_2019\Lesson_05.txt'
f = path.split("\\")[-1]
print(f"Имя файла из пути: {f}")

s = ['Буря', 'мглою', 'небо', 'кроет']
i = 0
while i < len(s):
    print(s[i])
    i += 1

s = ['Буря', 'мглою', 'небо', 'кроет']
i = 0
while i < len(s):
    if s[i] == 'мглою':
        i += 1
        continue
    print(s[i])
    i += 1

print('00000000011111111112222222222')
print('12345678901234567890123456789')
print('***\t***\t***\t***')
print('100\t100500\t1000\t10')

import random
print("-" * 13)
for i in range(10):
  a = str(random.randint(0,9))
  b = str(random.randint(0,9))
  c = str(random.randint(0,9))
  print(f"| {a} | {b} | {c} |")
print("-" * 13)


print("-" * 18)
for i in range(10):
  a = str(random.randint(0,99))
  b = str(random.randint(0,999))
  c = str(random.randint(0,9999))
  print(f"| {a:>4} | {b:>4} | {c:>4} |")
print("-" * 18)


print("-" * 25)
for i in range(10):
  a = str(random.randint(0,99))
  b = str(random.randint(0,999))
  c = str(random.randint(0,9999))
  print(f"| {a} \t| {b} \t| {c} \t|")
print("-" * 25)

print("-" * 25)
for i in range(10):
  a = str(random.randint(0,99))
  b = str(random.randint(0,999))
  c = str(random.randint(0,9999))
  print(f"| {a:>2} \t| {b:>3} \t| {c:>4} \t|")
print("-" * 25)


print("-" * 25)
for i in range(10):
  a = str(random.randint(0,99))
  b = str(random.randint(0,999))
  c = str(random.randint(0,9999))
  print(f"| {a:>4} \t| {b:>4} \t| {c:>4} \t|")
print("-" * 25)

