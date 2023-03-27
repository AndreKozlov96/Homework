# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

a = []
b = set()
n = int(input('Введите количество чисел первого набора: '))
m = int(input('Введите количество чисел второго набора: '))
print('Введите числа первого набора:')
for i in range(n):
    a.append(int(input()))
print('Введите числа второго набора:')
for j in range(m):
    number = int(input())
    if number in a:
        b.add(number)
print(sorted(list(b)))