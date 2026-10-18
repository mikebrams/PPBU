name = input()

YN = ['Не фото', 'Фото']

photo = name.lower().endswith((".jpg", ".jpeg", ".png"))

print(YN[photo])