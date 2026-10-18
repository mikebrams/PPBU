# breeds = input().split(", ")
# line = input()
# selection = () if line == "" else (int(line),)
#
# if not selection:
#     print('Сначала выберите породу')
# else:
#     print(f'Выбрано: {breeds[selection[0]]}')


prompt = input().strip().lower()
breeds = input().split(", ")
line = input()
selection = () if line == "" else (int(line),)

found = []

for breed in breeds:
    if prompt in breed:
        found.append(breed)


if not selection:
    print('Сначала выберите породу')
else:
    print(f'Выбрано: {found[selection[0]]}')

