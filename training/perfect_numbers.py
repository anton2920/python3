i = 0
s = 0
print('Perfect numbers: ')
while True:
    i += 1
    for j in range(1, (i // 2) + 1, 1):
        if i % j == 0:
            s += j
    if s == i:
        print(i, end='\n')
    s = 0
