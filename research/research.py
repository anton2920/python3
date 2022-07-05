def p(x):
    global a
    global k
    b = 0
    c = 0
    for i in range(int(k), -1, -1):
        b = b + int((int(a[c])) * int((x ** int(i))))
        c = c + 1
    return b


def main():
    a = []
    global k
    global a
    k = input()
    for i in range(0, int(k) + 1, 1):
        a.append(input())
    print(a)
    outputs = open('research.out', 'w')
    if (int(a[0]) > 0) and (int(k) != 3):
        for i in range(-100, 100):
            if (p(i) > p(i + 1)):
                pass
            elif (p(i) < p(i + 1)):
                if i > 0:
                    outputs.write('-100 ' + '+' + str(i) + ' down' + '\n')
                    outputs.write('+' + str(i) + ' +100' + ' up' + '\n')
                    break
                if i < 0:
                    outputs.write('-100 ' + str(i) + ' down' + '\n')
                    outputs.write(str(i) + ' +100' + ' up' + '\n')
                    break
    elif (int(a[0]) < 0) and (int(k) != 3):
        for i in range(-100, 100):
            if (p(i) > p(i + 1)):
                pass
            elif (p(i) < p(i + 1)):
                if i > 0:
                    outputs.write('-100 ' + '+' + str(i) + ' down', '\n')
                    outputs.write('+' + str(i) + ' +100' + ' up', '\n')
                    break
                if i < 0:
                    outputs.write('-100 ' + str(i) + ' down', '\n')
                    outputs.write(str(i) + ' +100' + ' up', '\n')
                    break
    elif int(k) == 3:
        outputs.write('-100 +100 up')
    outputs.close()
    inputs = open('research.out', 'r')
    test = inputs.read()
    if test == '':
        inputs.close()
        outputs = open('research.out', 'w')
        if int(a[0]) > 0:
            outputs.write('-100 +100 down')
        elif int(a[0]) < 0:
            outputs.write('-100 +100 up')
        outputs.close()
    else:
        inputs.close()


if __name__ == "__main__":
    main()
