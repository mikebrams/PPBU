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
            if string[i].islower() or string[i] == ' ':
                count += 2
            elif string[i].isupper():
                count += 1

        elif string[i-1].islower() or string[i-1] == ' ':
            if string[i].isupper():
                count += 2
            elif string[i].islower() or string[i] == ' ':
                count += 1

    if string[-1].isupper():
        count += 1

    print(count)