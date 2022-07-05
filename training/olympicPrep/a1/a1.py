def main():
    inputs = open('input.txt', 'r')
    all = inputs.read().split('\n')
    a = int(all[0])
    b = int(all[1])
    c = int(all[2])
    inputs.close()
    k = 0
    while (a <= b):
        if (a % c == 0):
            a += 50
            k += 1
        else:
            a += 1
    outputs = open('output.txt', 'w')
    outputs.write(str(k))


if __name__ == '__main__':
    main()