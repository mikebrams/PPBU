import sys
import pprint

base = {}

for line in sys.stdin:
    cour, dist, time = line.split()

    base.setdefault(cour, {'count': 0, 'total_time': 0, 'districts': {}})
    base[cour]['count'] += 1
    base[cour]['total_time'] += int(time)
    base[cour]['districts'][dist] = base.get(cour, {}).get('districts').get(dist, 0) + 1
    # base.setdefault(cour, {}).setdefault('districts', {}).setdefault(dist, 0)
    # base[cour]['districts'][dist] += 1

couriers = []
for k, v in base.items():
    courier = k
    count = v['count']
    mean_time = v['total_time'] / v['count']

    districts = v['districts']
    best_dict = min(districts, key=lambda district: (-districts[district], district))

    couriers.append((courier, count, mean_time, best_dict))

couriers.sort(key=lambda item: (-item[1], item[2], item[0]))

for i in couriers:
    print(f'{i[0]} {i[1]} {i[2]:.2f} {i[3]}')



"""
{'ivan': {'count': 3, 'total_time': 82, 'districts': {'north': 2, 'center': 1}},
 'anna': {'count': 2, 'total_time': 60, 'districts': {'center': 1, 'north': 1}},
 'petr': {'count': 1, 'total_time': 25, 'districts': {'center': 1}}}
"""