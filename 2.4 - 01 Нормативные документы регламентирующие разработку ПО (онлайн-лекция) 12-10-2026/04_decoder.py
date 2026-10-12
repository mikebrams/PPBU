key = input('Введите ключ шифрования: ')


with open('code.txt', 'r', encoding='utf-8') as f:
    s = f.read()


code_out = ''
for c in s:
    code = ord(c) - int(key)
    symbol = chr(code)
    code_out += symbol

with open('code_out.txt', 'w', encoding='utf-8') as f:
    f.write(code_out)


print(code_out)