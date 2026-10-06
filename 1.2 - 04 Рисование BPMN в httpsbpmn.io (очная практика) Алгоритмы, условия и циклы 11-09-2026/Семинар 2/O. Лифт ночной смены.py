"""
c = int(input())    # вместимость   1 ≤ c ≤ 1000
s = int(input())    # пассажиры     0 ≤ s ≤ c
n = int(input())    # кол-во операций
"""

c, s, n = map(int, input().split())

cancel = 0

for i in range(n):
    enter = int(input())

    if 0 <= s + enter <= c:
        s += enter
    else:
        cancel += 1

print(s, cancel)
