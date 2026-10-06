n = int(input())
books_list =[]
"""
В каждой строке выведите название книги, медиану её оценок и количество полученных оценок.
"""

def median(values):
    return values[count // 2]

for _ in range(n):
    input_data = input().split()

    book = input_data[0]    # название книги
    count = int(input_data[1])  # количество оценок
    marks = sorted(list(map(int, input_data[2:])))  # оценки

    med = median(marks)

    books_list.append((book, med, count))

books_list.sort(key=lambda x: (-x[1], -x[2], x[0]))

for i in books_list:
    print(*i)


"""
4
atlas 5 8 10 9 7 6
dune 3 9 9 7
orbit 5 9 5 9 8 8
zen 1 8

dune 9 3
atlas 8 5
orbit 8 5
zen 8 1
"""

a = ''