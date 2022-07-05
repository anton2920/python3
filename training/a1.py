# Обучение
import random  # Модуль для "работы" с случайными числами
a = []    # Инициализируем список. Индескация начинается с нуля
a.append('Hello')    # Наполняем список. append добавляет элемент в конец списка
a.append(3)
a.append([1, 2, 3])
print(a)
print(len(a))   # Выводим кол-во элементов в списке
a.remove(3)   # Удаляем элемент (со значением "3")
print(a)
print(len(a))
a.insert(0, 4)   # Добавляем элемент "4" на позицию "0"
print(a)
print(len(a))
print(a.count(4))  # Считаем кол-во элементов со значением "4"
a.reverse()   # Переворачиваем список (последний элемент становится первым, предпоследний вторым)
print(a)
a = list(range(101))    # Задаем список с элементами от 0 до 100
print(a)
a = list(range(50, 101,2))
print(a)
numbers = [1, 2, 3, 4, 5]
i = 0
length = len(numbers) - 1
while i <= length:
    print(numbers[i], end = ' ')
    i += 1
print()
for i in numbers:        # Цикл, для обхода списка
    print(i, end = ' ')



def smth():
    """Описание функции. Вызывается по 'help(smth)' или 'print(smth.__doc__)'"""
    pass
smth()
help(smth)
print()
print(smth.__doc__)


for i in range(10):
    print(random.randint(1, 100), end = ' ') # Генерация случайных целых чисел в диапазоне [1;100]


# Продолжение (Импортирование функции "randint" из модуля "random")
# from random import randint
# print(randint(1, 10))


# from math import * (Импортирование всех фунций и переменных из модуля "math")


# from math import sqrt, pi (Импортирование функции "sqrt" и переменной "pi" из модуля "math")

# from math import sqrt as mysqrt (Импортирование фунции "sqrt" из модуля "math" с названием "mysqrt")


# Срез списка
print("""

""")

digits = list(range(1, 11))
digits2 = digits[4]
print(digits)
print(digits2)
print(digits[2:5:1])   # Срез списка (получение элементов с [2] по [4]) c шагом 1
# print(digits[:5:1])    Срез списка по [4] с шагом 1
# print(digits[2::1])    Срез списка с [2] с шагом 1

