n = int(input())    # кол-во линий метро 1 <= n <= 50

lines = {}
station_lines = {}

stations = set()

for i in range(n):
    line, k, *stans = input().split()    # линия, 1 <= число станций <= 100, названия станций

    stations.update(stans)

    lines[line] = set(stans)

    for station in stans:
        station_lines.setdefault(station, set())
        station_lines[station].add(line)


q = int(input())    # кол-во запросов 1 <= q <= 2000
routes = []
for i in range(q):
    routes.append(input().split())

for i in range(len(routes)):

    start = routes[i][0]
    finish = routes[i][1]

    if start not in stations or finish not in stations:
        print(-1)
        continue
    else:

        start_line = station_lines[start]
        finish_line = station_lines[finish]

        direct = start_line & finish_line

        if direct:
            print(0, min(direct))

        else:
            transfers = []
            for j in start_line:
                for k in finish_line:
                    common = lines[j] & lines[k]
                    if common:
                        transfers.append([*common, j, k])
            if transfers:
                res = min(transfers)
                print(1, res[1], res[0], res[2])
            else:
                print(-1)



"""
3
red 4 a b c d
blue 3 c e f
green 3 f g h
5
a d
a e
a h
e h
x a

0 red
1 red c blue
-1
1 blue f green
-1
"""