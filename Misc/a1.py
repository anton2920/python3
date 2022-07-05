import math
a = float(input('Type first number: '))
znak = str(input('Type math sign: '))
b = float(input('Type second number: '))
c = None
if znak == '+':
    c = a + b
elif znak == '-':
    c = a - b
elif znak == '*':
    c = a * b
elif znak == '/':
    if b != 0:
        c = a / b
    else:
        print('Big mistake!!!')
else:
    print('Operation is not supported!!!')        
if c:
    print('Answer: ', c)