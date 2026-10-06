def normalize(phone):
    phone = ''.join(ch for ch in phone if ch in '0123456789')

    if len(phone) == 10:
        phone = '7' + phone
    elif len(phone) == 11 and (phone[0] == '7' or phone[0] == '8'):
        phone = '7' + phone[1:]
    else:
        return None

    return phone


numbers = set()
invalid = 0

n = int(input())
for i in range(n):
    digits = normalize(input())

    if digits:
        digits = f'+7({digits[1:4]}){digits[4:7]}-{digits[7:9]}-{digits[9:]}'
        numbers.add(digits)
    else:
        invalid += 1

print(len(numbers), invalid)

for number in sorted(numbers):
    print(number)
