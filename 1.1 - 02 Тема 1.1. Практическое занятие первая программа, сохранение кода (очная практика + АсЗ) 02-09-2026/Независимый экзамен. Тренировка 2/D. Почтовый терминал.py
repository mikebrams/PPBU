terminals = [['Atlas', 'Borealis', 'Cygnus'],
             ['Draco', 'Equuleus', 'Fornax'],
             ['Gemini', 'Hydra', 'Indus']]

num = int(input())

steps = 0
current_terminal = 0

for i in range(num):
    term = input()
    if term in terminals[current_terminal]:
        continue
    else:
        for j in range(3):
            if term in terminals[j]:
                steps = steps + abs(current_terminal - j)
                current_terminal = j

# Atlas
# Gemini
# Draco
# Fornax
# Borealis

print(steps)