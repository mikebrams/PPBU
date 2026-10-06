import pprint

# for i in range(0, 256):
#     print(f'Символ {chr(i)} код символа {i}')

# kaomoji.ru

smile = '( ˘⌣˘)♡(˘⌣˘ )'

for i in smile:
    print(f'Код символа {i} - {ord(i)}')


print(chr(9825))

print(f'Катя{chr(128512)}Миша')



s = ["С", "новым", "годом!"]
text = " ".join(s)
print(text)  # Вывод: С новым годом!


s = ["C:", "Python", "Scripts", "Join_1.py"]
text = "\\".join(s)
print(text)

s = ["https:", "", "trinket.io", "docs", "colors"]
text = "/".join(s)
print(text)

s = ["Царь недолго собирался:",
     "В тот же вечер обвенчался.",
     "Царь Салтан за пир честной",
     "Сел с царицей молодой;"]
text = "\n".join(s)
print(text)
