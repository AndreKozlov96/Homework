# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

a1 = int(input('Введите первый элемент прогрессии a1: '))
n = int(input('Введите количество элементов n: '))
d = int(input('Введите шаг прогрессии d: '))
ar_prog = []
for i in range(1, (n + 1)):
    ar_prog.append(a1 + (i - 1) * d)
print(ar_prog)
