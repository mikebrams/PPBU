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

found = []

for breed in breeds:
    if prompt in breed:
        found.append(breed)

if not prompt:
    for breed in breeds:
        print(breed)
elif not found:
    print('Ничего не найдено')
else:
    for breed in found:
        print(breed)

