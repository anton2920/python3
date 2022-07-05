def main():
    a = []
    b = []
    inputs = open('money.in', 'r')
    a = inputs.read().split('\n')
    inputs.close()
    for i in range(0, len(a), 1):
        b.append(int(a[i]))
    del(a)
    item = -1
    for i in range(0, len(b), 1):
        if b.count(b[i]) >= len(b) // 2:
            item = str(b[i])
            break
    if max != -1:
        outputs = open('money.out', 'w')
        outputs.write(item)
        outputs.close()


if __name__ == '__main__':
    main()