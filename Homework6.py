# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Пример:
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
#
# a1 = int(input("\nВведите первый элемент последовательности: "))
# d = int(input("\nВведите разность арефмитической прогресси: "))
# n = int(input("\nКоличесвто элементов прогрессии: "))
# an = []
#
# for i in range(n):
#     an.append(a1 + (n - 1) * d)
#     n -= 1
# print(f"\nАрифметическая прогрессия в заданном диапазоне: ", *sorted(an))
# input("\n\tPress Enter to Exit")

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Пример:
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# from random import randint
#
# min_value = int(input("Введите минимальное значение диапазона: "))
# max_value = int(input(("Введите максимально значение диапазона: ")))
# print("\nНачальный список")
# print(my_list := [randint(0, 10) for _ in range(1, 20)])
# print("\nДиапазон значений")
# print(range_value := [i for i in range(min_value, max_value + 1)])
# print(f"\nИндексы Элементов списка встречающиеся в диапазоне от {min_value} до {max_value} ")
# print(index_list := [i for i in range(len(my_list)) if my_list[i] in range_value])
# input("\n\tPress Enter to Exit")
