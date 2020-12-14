from operator  import itemgetter

fruits_quantity = {
    'イチゴ': 21,
    'ウメ': 51,
    'リンゴ': 14,
    'ナシ': 78,
    'バナナ': 2,
    'スイカ': 21,
}

print(fruits_quantity.items())
fruits_sorted = sorted(fruits_quantity.items(), key=itemgetter(1), reverse=True)
for fruit, quantity in fruits_sorted:
    print(fruit + '->' + str(quantity))