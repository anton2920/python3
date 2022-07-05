def orep():
    global inputs
    inputs = open('input.txt', 'r')


def orep2():
    global outputs
    outputs = open('output.txt', 'w')


def main():
    orep()
    b = inputs.read()
    inputs.close()
    maxi = 0
    d = int(b)
    for i in range(0, len(b), 1):
        a = []
        for i1 in range(0, len(b), 1):
            a.append(int(b[i1]))
        for j in range (1, 10, 1):
            a[i] = j
            c = ''
            for k in range(0, len(b), 1):
                c = c + str(a[k])
            c = int(c)
            if ((c % 3 == 0) and (c != d) and (c > maxi)):
                maxi = c
    orep2()
    outputs.write(str(maxi))
    outputs.close()


if __name__ == '__main__':
    main()