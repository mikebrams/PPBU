h, w = map(int, input().split())

puh = 0

for i in range(h):
    enter = sum(list(map(int, input().split())))
    puh += enter

print(puh)