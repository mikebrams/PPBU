text = input().lower().split()

if len(text) == 2:
    print(f'https://dog.ceo/api/breed/{text[0]}/{text[1]}/images/random')
elif len(text) == 1:
    print(f'https://dog.ceo/api/breed/{text[0]}/images/random')
else:
    print('Неверная порода')

