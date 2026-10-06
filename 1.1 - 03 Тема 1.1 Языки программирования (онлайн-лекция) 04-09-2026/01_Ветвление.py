# константа - набирается ЛЬШИМИ

PI = 3.14

# ------------------------------

color = input('Цвет светофора: ')
match color:
    case 'red' | 'no': print('STOP')    # | - означает "или"
    case 'green': print('GO')
    case 'yellow': print('Ready')
    case _:print('цвет', color)  # Аналог "else"
