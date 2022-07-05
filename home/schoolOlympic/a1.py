def orep():
    global inputs
    inputs = open('input.txt', 'r')


def orep2():
    global outputs
    outputs = open('output.txt', 'w')


def main():
    orep()
    k = int(inputs.read())
    inputs.close()
    a = 0
    i = 1
    while (a != k):
        i += 1
        a = 0
        i1 = i
        while (i1 != 1):
            if (i1 % 3 == 0):
                i1 = i1 // 3
                a += 1
            else:
                i1 = i1 - 1
                a += 1
    orep2()
    outputs.write(str(i))
    outputs.close()

if __name__ == '__main__':
    main()