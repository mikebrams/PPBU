def choose_bait(baits: list[tuple[int, int]], reach):
    best = 0, 0
    for i in baits:
        if i[0] <= reach and i[1] > best[1]:
            best = i
    return baits.index(best) if best in baits else -1




print(choose_bait([(2, 5), (8, 100), (3, 5)], 3))
print(choose_bait([(5, 9)], 2))
print(choose_bait([], 0))
print(choose_bait([(0, 0)], 0))
print(choose_bait([(1, 7), (0, 7)], 1))
