string = input()

count = 0

if not string:
    print(0)
else:
    if string[0].isupper():
        count += 2
    else:
        count += 1


    for i in range(1, len(string)):

        if string[i-1].isupper():
            if string[i].islower():
                count += 2
            elif string[i].isupper():
                count += 1

        elif string[i-1].islower():
            if string[i].isupper():
                count += 2
            elif string[i].islower():
                count += 1

    if string[-1].isupper():
        count += 1

    count += string.count(' ')


    print(count)