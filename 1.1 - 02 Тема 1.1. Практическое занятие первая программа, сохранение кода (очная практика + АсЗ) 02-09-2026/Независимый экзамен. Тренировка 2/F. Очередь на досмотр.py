length, sec = map(int, input().split())
queue = input()

for i in range(sec):
    queue = queue.replace('AB', 'BA')

print(queue)