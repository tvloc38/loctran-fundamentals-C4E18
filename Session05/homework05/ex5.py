prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}

for k in prices:
    print(k)
    print('price :',prices[k])
    print('stock :',stock[k])
    print()

total = 0
for k in prices:
    money = prices[k] * stock[k]
    total += money
print('total money: {0}$'.format(total))