# Файлы

# Режимы открытия файла:
# r - чтение
# w - перезапись
# a - добавление
# b - Binary mode  Для картинок, аудио и т.д.
def orep():
    global inputs
    inputs = open('input.txt', 'r')  # Открытие файла "input.txt" на чтение (присвоение файла переменной "inputs")
orep()
print(inputs.read())  # Прочитать все содержимое файла
orep()
print('In file, there are ' + str(len(inputs.read())) + ' symbols')  # Найти количество символов в файле
inputs.close()   # Закрыть файл
# print(inputs.read(6))    Вывести на экран только 6 байт этого файла
# Здесь выполняется чтение, с той же позиции, где мы закончили в прошлый раз
def orep2():
    global outputs
    outputs = open('output.txt', 'w')   # Открытие/создание файла "output.txt" на запись (присвоение файла переменной "outputs")
orep2()
outputs.write('Hellooooo, World')  # Запись строки в файл
outputs.close()

def orep3():
    global outputs
    outputs = open('output.txt', 'a')
orep3()
outputs.write('!')
outputs.close()

orep()
a = inputs.readlines()  # Составить список из строк
print(a)

for i in a:               # Вывод строк через for
    print(i, end = '')
inputs.close()
print()


with open('input.txt', 'r') as inputs:
    print(inputs.read())




