from string import digits, ascii_letters
import re
import random

regex = r'^[+0-9]9\d{9,10}'

phone_number = '89991234567'
res = re.fullmatch(regex, phone_number)
if res:
    print(phone_number)
else:
    print('неправильный номер ТЛФ')