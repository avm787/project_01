# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"
count = 0
count1 = 0
for k1, v1 in titles.items():
    for k2, v2 in store.items():
        if v1 == k2:
            for i in range(len(store.get(v1))):                            
                count += store.get(v1)[i].get('quantity')
                count1 += store.get(v1)[i].get('quantity')*store.get(v1)[i].get('price')
            print(k1, '-', count, 'шт,', 'стоимость', count1, 'руб')             
            count = 0
            count1 = 0  
      
            
    


# for k1, v1 in titles.items():
#     # print(store.get(v1))
#     # print(titles.get(k1))
#     print(titles.keys(i))
#     for i in range(len(store.get(v1))):
#         # print(store.get(v1)[i].get('quantity') * store.get(v1)[i].get('price'))
#         sm += store.get(v1)[i].get('quantity') * store.get(v1)[i].get('price')
       



