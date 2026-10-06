"""
ученик                  name
общий_балл                  mark1 + mark2 + mark3 + ..... - сумма балов по всем предметам             
количество_предметов        len(name[subj])                     count
сильнейший_предмет      subj[mark1 + mark2 + ...]
балл_по_предмету        mark

anna 16 3 math 9
boris 13 2 history 10
clara 12 3 history 4

10
anna math 5
anna math 4
anna physics 5
boris math 3
boris history 5
boris history 5
clara physics 4
clara math 4
clara history 4
anna history 2

"""
inpt = [10, 'anna math 5', 'anna math 4', 'anna physics 5', 'boris math 3', 'boris history 5',
     'boris history 5', 'clara physics 4', 'clara math 4', 'clara history 4', 'anna history 2']

# n = int(input())
# stud_dict = {}
#
# for i in range(n):
#     name, subj, mark = input().split()
#
#     if name not in stud_dict:
#         stud_dict[name] = {}
#
#     if subj not in stud_dict[name]:
#         stud_dict[name][subj] = [1, int(mark)]
#     else:
#         stud_dict[name][subj][0] += 1               # subj count
#         stud_dict[name][subj][1] += int(mark)       # total points for subj




stud_dict = {'anna': {'math': [2, 9], 'physics': [1, 5], 'history': [1, 2]}, 'boris': {'math': [1, 3], 'history': [2, 10]}, 'clara': {'physics': [1, 4], 'math': [1, 4], 'history': [1, 4]}}

best_subj = []

a = len(stud_dict)

for key in stud_dict.keys():
    stud = []
    total_points = 0
    for value in stud_dict[key]:
        total_points += stud_dict[key][value][1]
        stud.append([key, value, stud_dict[key][value][0], stud_dict[key][value][1], len(stud_dict[key]) ])

        # ученик, предмет, кол-во оценок по предмету, сумма оценок по предмету, всего предметов, сумма всех оценок



    stud.sort(key=lambda x: (-x[3], -x[2], x[1]))

    best_subj.append(tuple(stud[0]+[total_points]))



    # (-points, -count, subject) сильнейший предмет: всего баллов по предмету, кол-во оценок по предмету, предмет


print(best_subj)

# for i in range(n):
#     print(name, subj, mark, sep=' ')
