from string import digits, ascii_letters
import re
import random

def get_rassword(m):
    # data = set(ascii_letters + digits) - {'0', '1', 'o', 'O', 'l', 'I'}
    # data = ''.join(data)

    data1 = ''.join(re.findall(r'[^01oOlI]', ascii_letters + digits)) # все знаки кроме 01oOlI
    print(data1)
    password = random.sample(data1, m)
    print(password)
    # pos = random.sample(range(m), 3)
    # password[pos[0]] = password[pos[0]].lower()
    # password[pos[1]] = password[pos[1]].upper()
    # password[pos[2]] = str(random.randint(2, 9))

    password = ''
    while not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password) or not re.search(r'[2-9]', password):
        password = ''.join(random.sample(data1, m))

    return password

print('--------------------')
print(get_rassword(8))
print('--------------------')

# def main(n, m):
#     res = set()
#     while len(res) < n:
#         res.add(get_rassword(m))
#
#     for p in res:
#         print(p)
#
# main(10, 8)