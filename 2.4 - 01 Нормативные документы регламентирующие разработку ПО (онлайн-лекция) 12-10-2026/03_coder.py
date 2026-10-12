with open('text.txt', 'r', encoding='utf-8') as f:
    s = f.read()


key = input('Введите ключ шифрования: ')
secret = ''
for c in s:
    code = ord(c)+ int(key)
    symbol = chr(code)
    secret += symbol

with open('code.txt', 'w', encoding='utf-8') as f:
    f.write(secret)


print(secret)