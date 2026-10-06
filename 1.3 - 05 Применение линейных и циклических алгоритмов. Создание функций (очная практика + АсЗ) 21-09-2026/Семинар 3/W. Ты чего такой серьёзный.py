string = input()

str2 = string.replace(':-(', '[{}]')
str3 = str2.replace(':(', ':)')
str4 = str3.replace('[{}]', ':-(')

print(str4)