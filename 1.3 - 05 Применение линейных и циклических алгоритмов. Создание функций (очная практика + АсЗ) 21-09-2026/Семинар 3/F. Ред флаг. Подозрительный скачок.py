a, b, k = map(int, input().split())

print('FLAG' if abs(a - b) > k else 'OK')