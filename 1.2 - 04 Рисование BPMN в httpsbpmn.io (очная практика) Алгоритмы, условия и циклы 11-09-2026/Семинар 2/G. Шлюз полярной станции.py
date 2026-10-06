p = int(input())    # наличие пропуска (0 или 1)
a = int(input())    # тревога (0 или 1)
c = int(input())    # уровень человека (от 0 до 3)
r = int(input())    # требуемый уровень (от 1 до 3)


if a:
    print('LOCKDOWN')
elif not p:
    print('NO_PASS')
elif c < r:
    print('DENIED')
else:
    print('ACCESS')
