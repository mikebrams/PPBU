txt = input()
journal = ''


for i in range(len(txt)):
    if txt[i].isalpha():
        journal += txt[i]
    else:
        journal = journal[:len(journal)-1]

print(journal)
