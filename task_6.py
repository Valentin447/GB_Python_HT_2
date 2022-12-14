'''
6) *Реализовать структуру данных «Товары». Она должна представлять собой список
 кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже
 должно быть два элемента — номер товара и словарь с параметрами
 (характеристиками товара: название, цена, количество, единица измерения).
 Структуру нужно сформировать программно, т.е. запрашивать все данные у
 пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
ключ — характеристика товара, например название, а значение — список
значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
'''

products = []
count = 1
esc = 0
while esc == 0:
    name = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    units = input("Введите единицы измерения: ")
    products.append((count, {"название": name, "цена": price,
                             "количество": quantity, "eд": units}))
    for el in products:
        print(el)
    out = input("Нажмите Enter чтобы добавить ещё товар или введите 0 "
                "чтобы закончить ввод: ")
    if out == "0":
        esc = 1
    count = count + 1

name_list = []
price_list = []
quantity_list = []
units_list = []
for el in products:
    product_dict = el[1]
    name_list.append(product_dict.get("название"))
    price_list.append(product_dict.get("цена"))
    quantity_list.append(product_dict.get("количество"))
    units_list.append(product_dict.get("eд"))
analitics_dict = {"название": list(set(name_list)),
                  "цена": list(set(price_list)),
                  "количество": list(set(quantity_list)),
                  "eд": list(set(units_list))}
print("Аналитика:")
for el in analitics_dict:
    print(f"{el}: {analitics_dict.get(el)}")
