# Иключения: (основные)
# ImportError проблема с имортом модулей
# IndexError проблема с индексом списка (всего 100, но мы выводим 105)
# NameError проблема с переменной или чем-то, имя чего-то мы не указали
# SyntaxError проблема с синтаксисом
# TypeError проблема с типами (например при конкатенации)
# ValueError проблема со значением (строка вместа булеана)
# ZeroDivisionError деление на ноль
try:
    # eval('print(7 / 0)a') # Чтобы поймать SyntaxError (не рекомендуется)
    print(7 / 0)
except ZeroDivisionError:  # Ловится исключение деления на ноль
    print('Don\'t divide by 0')
    pass
except SyntaxError:
    print('You\'re idiot!')
# except (SyntaxError, NameError):   ловить много сразу
# except:  ловить все
finally:   # Выводится в не зависимости от того, было что-то поймано или нет
    print('Bye!')
print('Hello!')
print()
try:
    pogoda = 'bad'
    if pogoda == 'bad':
        raise TypeError  # Поднять TypeError
except:
    print('Badf')

# i = 1
# if i == 1:
#    raise TypeError('Life is bad!') # Поднять TypeError c комментарием "Life is bad"

#class Popa(Exception):    Создание собственного исключения
#    pass

# raise Popa('Life is bad!')


def a1(text):
    assert text != ''  # Условие, если мы ничего не передаем в функцию, то выбросится исключение
    print(str(text) + '!')
a1('Hello world')

def a2(number):
    assert number > 0, "Number must be positive!"  # Условие, проверяющее, что на вход функции передается положительное число. При не выполнении условия выбросится AssertError с комментарием
    print(str(number))

a2(-110)
