def orep():
    global inputs
    inputs = open('input.txt', 'r')


def orep2():
    global outputs
    outputs = open('output.txt', 'w')


def main():
    orep()
    a = inputs.read()
    inputs.close()
    b = bin(int(a))
    b = b[2::]
    k = 0
    k1 = 0
    for i in range(0, len(b), 1):
        if (int(b[i]) == 1):
            k += 1
        else:
            k = 0
        if (k > k1):
            k1 = k
    orep2()
    if (k1 > k):
        outputs.write(str(k1))
    else:
        outputs.write(str(k))
    outputs.close()


if __name__ == '__main__':
    main()