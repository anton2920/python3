# Массивы
import random
a = []
b = []
s = 0
N = 5
for i in range(N):
    for j in range(N):
        b.append(random.randint(1, 100))
        s += b[j]
    a.insert(i, b)
    b = []
   # for j in range(N):            Примитивный вывод
   #     print(a[i][j], end=' ')
    print(' '.join(map(str, a[i])))
print('Summ is: ' + str(s))

print()
a = []
b = []
s = 0
N = 0
c = []
inputs = open('array.txt', 'r')
for i in range(10):
    for j in range(10):
        b.append((inputs.read(2)))
        if b[j] != '':
            c.append(int(b[j]))
            s = s + c[j]
        if (b[j].find('\n') != -1) or b[j] == '':
            break
    a.append(c)
    if b[j] == '':
        break
    b = []
    c = []
    print(' '.join(map(str, a[i])))
print('The file summ is: ', s)
inputs.close()
