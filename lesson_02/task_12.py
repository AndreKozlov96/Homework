# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает
# две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import random

x = random.randint(1, 1001)
y = random.randint(1, 1001)
x1 = 0
y1 = 0
print(x, y)
s = x + y
p = x * y
print(s, p)
for i in range(1001):
    for k in range(1001):
        x1, y1 = ((i, k) if (i + k == s) and (i * k == p) else (x1, y1))
print(f'Задуманные числа X = {x} и Y = {y}')
