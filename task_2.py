"""
2) Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = []
while True:
    value = input("Введите значения элемента "
                  "или пустую строку для продолжения: ")
    if value == "":
        break
    my_list.append(value)
    print(my_list)

count = 0
while count < len(my_list):
    if count % 2 != 0:
        my_list[count - 1], my_list[count] = my_list[count], my_list[count - 1]
    count = count + 1
print(f"Результат: {my_list}")
