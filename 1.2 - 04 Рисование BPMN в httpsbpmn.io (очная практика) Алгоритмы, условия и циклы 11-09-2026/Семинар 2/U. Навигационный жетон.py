n = int(input())
n_zero = n

quantity_of_nums = 0
quantity_of_zero = 0
max_num = 0
sum_of_nums = 0

sign = -1

while n:
    sign *= -1
    num = n % 10

    quantity_of_nums += 1
    sum_of_nums += (num * sign)

    if num == 0:
        quantity_of_zero += 1
    if num > max_num:
        max_num = num

    n //= 10

if n_zero == 0:
    print(1, 1, 0, 0, sep=' ')
else:
    print(f'{quantity_of_nums} {quantity_of_zero} {max_num} {sum_of_nums}')