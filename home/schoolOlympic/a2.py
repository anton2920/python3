def orep():
    global inputs
    inputs = open('input.txt', 'r')


def orep2():
    global outputs
    outputs = open('output.txt', 'w')


def main():
    orep()
    a = []
    min = 40001
    n = (inputs.read().split())
    for i in range(0, int(n[0]), 1):
        a1 = int(n[i+1])
        a.append(a1)
    inputs.close()
    for i in range(0, int(n[0]), 1):
        for j in range(0, int(n[0]), 1):
            if (i == j):
                continue
            if ((min > a[i] * a[j]) and ((a[i] * a[j]) % 2 != 0)):
                min = a[i] * a[j]
    orep2()
    if (min == 40001):
        outputs.write('нет')
    else:
        outputs.write(str(min))
    outputs.close()


if __name__ == '__main__':
    main()