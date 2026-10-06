products = {}

for i in range(int(input())):
    name, price, stock = input().split()
    price, stock = int(price), int(stock)

    products[name] = [price, stock, 0]    # товар: [цена, остаток, накопленная выручка]

completed_request = 0
rejected_request = 0
total_revenue = 0

for j in range(int(input())):
    name, quantity = input().split()    # запрошенный товар, кол-во
    quantity = int(quantity)

    if name not in products or (name in products and products[name][1] < quantity):
        rejected_request += 1
        continue
    elif name in products and products[name][1] >= quantity:  # заказ есть на складе и кол-ва достаточно
        products[name][1] -= quantity
        revenue = products[name][0] * quantity
        products[name][2] += revenue

        completed_request += 1
        total_revenue += revenue

products_list = [(key, *val) for key, val in products.items()]
products_list.sort(key=lambda x: (x[2], -x[3], x[0]))

print(completed_request, rejected_request, total_revenue)
for i in products_list:
    print(i[0], i[2], i[3])