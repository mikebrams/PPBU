# n = int(input())
#
# used = set()
# next_number = {}
#
# for _ in range(n):
#     name = input()
#
#     if name in used:
#
#         k = next_number[name]
#
#         Flag = True
#
#         while Flag:
#
#             new_name = f'{name}{k}'
#
#             if new_name not in used:
#
#                 print(new_name)
#                 used.add(new_name)
#                 next_number[new_name] = k
#                 Flag = False
#
#             k += 1
#
#     else:
#         print('OK')
#         used.add(name)
#         next_number[name] = 1




n = int(input())

used = set()
next_number = {}

for _ in range(n):
    name = input()

    Flag = True

    while Flag:

        if name not in used:
            print('OK')
            used.add(name)
            next_number[name] = 1
            Flag = False

        else:

            k = next_number[name]

            new_name = f'{name}{k}'


            # print(new_name)
            used.add(new_name)
            next_number[new_name] = k
            Flag = False

            k += 1

    print(new_name)


"""         нужно       дает        следующее имя
5
user        OK          ОК          user:   1
user1       OK          ОК          user1:  1
user        user2       user1       
user1       user11      user11
user        user3       user2
user2       user21      ОК

5
user
user1
user
user1
user

"""


names_dict = {'user': 0, 'user1': 0}