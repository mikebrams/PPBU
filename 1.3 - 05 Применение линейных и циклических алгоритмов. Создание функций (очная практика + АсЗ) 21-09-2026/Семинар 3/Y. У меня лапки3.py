string = input()

space = string.count(' ')

new_string = ''.join(string.split())

count = 0

if not string:
    print(0)
elif not new_string:
    print(space)
else:
    if new_string[0].isupper():
        count += 2
    else:
        count += 1

    for i in range(1, len(new_string)):

        if new_string[i-1].isupper():
            if new_string[i].islower():
                count += 2
            else:
                count += 1

        else:
            if new_string[i].isupper():
                count += 2
            else:
                count += 1

    if new_string[-1].isupper():
        count += 1

    count += space

    print(count)