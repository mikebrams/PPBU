# file = open('text.txt', 'r', encoding='utf-8')
# print(file.read())
# print(file.read())
# file.close()
#
# file = open('text.txt', 'r', encoding='utf-8')
# print(file.readlines())
# file.close()
#
# file = open('text.txt', 'r', encoding='utf-8')
# s = file.read()
# print(s)
# file.close()

# for i in open('text.txt', 'r', encoding='utf-8'):
#     print(i)

with open('text.txt', 'r', encoding='utf-8') as f:
    ls = f.read().title().split()

ls.sort()
print(ls)


with open('text1.txt', 'w', encoding='utf-8') as f:
    for n, i in enumerate(ls, 1):
        f.write(f'{n}. {i}\n')