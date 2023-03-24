# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите положительное число N: '))
k = 0
degree = 2 ** k
while degree < n:
    print(degree, end=' ')
    k += 1
    degree = 2 ** k
print('\n')
'''
Есть более элегантное на мой взгляд решение:
'''
import math

n = int(input('Введите положительное число N: '))
k = int(math.log2(n))
print([2 ** i for i in range(k + 1)])
