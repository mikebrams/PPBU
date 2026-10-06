"""
Для каждого пользователя определите его итоговое местоположение, количество корректных и ошибочных событий.

Пользователей выведите в следующем порядке:

- по убыванию количества ошибочных событий;
- при равенстве — по убыванию количества корректных событий;
- затем по имени в лексикографическом порядке.
"""


users = {}
rooms = {}
valid_count, invalid_count = 0, 0

maximum = 0

for i in range(int(input())):
    name, room, action = input().split()

    rooms.setdefault(room, [0, 0])

    users.setdefault(name, [None, 0, 0])

    if name not in users:
        users[name] = [None, 0, 0]      # [location, valid_count, invalid_count]

        if action == 'enter':           # корректный вход
            users[name][0] = room
            users[name][1] += 1
            valid_count +=1

            rooms[room][0] += 1  # увеличиваем текущее кол-во пользователей в комнате
            rooms[room][1] += 1  # обновить максимум

        else:
            users[name][2] += 1
            invalid_count += 1

    else:
        if action == 'enter':
            if users[name][0] is None:
                users[name][0] = room
                users[name][1] += 1
                valid_count += 1

                rooms[room][0] += 1  # увеличиваем текущее кол-во пользователей в комнате
                rooms[room][1] += 1  # обновить максимум
            else:
                users[name][2] += 1
                invalid_count += 1
        else:                            # корректный выход
            if users[name][0] == room:
                users[name][0] = None
                users[name][1] += 1
                valid_count += 1

                rooms[room][0] -= 1  # уменьшаем текущее кол-во пользователей в комнате
            else:
                users[name][2] += 1
                invalid_count += 1


users_list = [(key, *val) for key, val in users.items()]    # name, location, valid_count, invalid_count
rooms_list = [(key, *val) for key, val in rooms.items()]    # room, current, maximum

users_list.sort(key=lambda x: (-x[3], -x[2], x[0]))
rooms_list.sort(key=lambda x: (-x[2], -x[1], x[0]))


print(valid_count, invalid_count)
print(f'USERS {len(users)}')
for i in users_list:
    print(f'{i[0]} {'outside' if i[1] is None else i[1]} {i[2]} {i[3]}')

print(f'ROOMS {len(rooms)}')
for j in rooms_list:
    print(f'{j[0]} {j[1]} {j[2]}')


"""
8
anna lab enter
boris lab enter
anna office enter
anna lab exit
anna lab exit
boris office exit
boris lab exit
clara office exit

4 4
USERS 3
anna outside 2 2
boris outside 2 1
clara outside 0 1
ROOMS 2
lab 0 2
office 0 0

"""