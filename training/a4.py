# Словари
a = {
    "LetterA" : "Apple",
    "LetterB" : "Banana"
}
key = input('Type Key: ')
try:
    print(a[key])
except KeyError:
    print('Error!')

#   Вместо исключения можно сделать так:
# print(a.get(key, "Error!"))


# Кортеж (что-то типа константного списка)

a = (1, 2, 3, 4, 5)  # Задание кортежа

# При попытке добавления элемента поднимает TypeError

a = 1, 2, 3, 4, 5  # Тоже самое

print(a)
