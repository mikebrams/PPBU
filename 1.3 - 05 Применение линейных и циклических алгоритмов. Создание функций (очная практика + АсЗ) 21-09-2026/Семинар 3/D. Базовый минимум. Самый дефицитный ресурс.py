b, s, t = map(int, input().split()) # 5 7 20

kit = min(b // 1, s // 2, t // 3)

b_used = kit * 1
s_used = kit * 2
t_used = kit * 3

b_rest = b - b_used
s_rest = s - s_used
t_rest = t - t_used

dokup_b = max(0, 1 - b_rest)
dokup_s = max(0, 2 - s_rest)
dokup_t = max(0, 3 - t_rest)

print(kit)
print(dokup_b, dokup_s, dokup_t)