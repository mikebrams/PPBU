# Независимый экзамен. Тренировка 3. Задача K. Рейтинг кинофестиваля

import sys

films = {}

for line in sys.stdin:
    name, film, mark = line.split()

    films.setdefault(film, []).append(int(mark))

films_out = []

def average(scores):
    return sum(scores) / len(scores)

for film, marks in films.items():

    films_out.append([film, average(marks), max(marks), min(marks), len(marks)])

films_out.sort(key=lambda item: (-item[1], -item[4], item[0]))

for i in films_out:
    print(f'{i[0]} {i[1]:.2f} {i[2]} {i[3]} {i[4]}')