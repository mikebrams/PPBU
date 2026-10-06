players, tasks = map(int, input().split())

max_spread = -1
player_num = 1
player_results = 0

for i in range(1, players + 1):
    results = list(map(int, input().split()))

    spread = max(results) - min(results)

    if spread > max_spread:
        max_spread = spread
        player_num = i
        player_results = sorted(results)

print(player_num)
print(*player_results)
