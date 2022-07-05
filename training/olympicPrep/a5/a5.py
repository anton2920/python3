def main():
    inputs = open('input.txt', 'r')
    a = inputs.read()
    while True:
        sum1 = 0
        sum2 = 0
        a = str(int(a) + 1)
        if len(a) % 2 != 0:
            a = '0' + a
        for i in range(len(a) // 2):
            sum1 += int(a[i])
        for i in range(len(a) - 1, (len(a) // 2) - 1, -1):
            sum2 += int(a[i])
        if sum1 == sum2:
            break
    outputs = open('output.txt', 'w')
    outputs.write(a)
    outputs.close()


if __name__ == '__main__':
    main()