n, m = map(int, input().split())

n_kup = list(map(int, input().split()))
m_kod = list(map(int, input().split()))

tries = ['NO' for i in range(m)]

for i in range(m):
    if m_kod[i] in n_kup:
        n_kup.remove(m_kod[i])
        tries[i] = 'YES'

print(*tries)
print(len(n_kup))
print(*sorted(n_kup) if n_kup else '')
