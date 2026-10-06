def name(nm):
    cnt = 0
    def surname(snm):
        nonlocal cnt
        cnt += 1
        print(cnt, nm, snm)
    return surname

# name('Mary')('Petrova')


sur = name('Mary')
sur1 = name('Mik')
sur('Knyzhna')
sur('Knyzhna')
sur('Knyzhna')
sur1('Dundee')
sur1('Brams')




