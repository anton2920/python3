def orep():
    global inputs
    inputs = open('input.txt', 'r')


def orep2():
    global outputs
    outputs = open('output.txt', 'w')


def main():
    orep()
    vse = inputs.read().split()
    inputs.close()
    a = str(int(vse[0]) + int(vse[1]))
    k = 0
    for i in range(1, len(a), 1):
        if (a[i - 1] == a[i]):
            k = 1
            break
    orep2()
    if (k == 1):
        outputs.write('есть')
    else:
        outputs.write('нет')
    outputs.close()


if __name__ == '__main__':
    main()