def main():
    inputs = open('input.txt', 'r')
    all = inputs.read().split()
    a = int(all[0])
    b = int(all[1])
    c = int(all[2])
    inputs.close()
    sred = 0
    ocenki = []
    ans = 0
    not_four = True
    for i in range(0, a, 1):
        ocenki.append(2)
    for i in range(0, b, 1):
        ocenki.append(3)
    for i in range(0, c, 1):
        ocenki.append(4)
    while not_four:
        for i in range(0, len(ocenki), 1):
            sred += ocenki[i]
        sred = sred / len(ocenki)
        if round(sred) >= 4:
            not_four = False
        else:
            ocenki.append(5)
            ans += 1
            sred = 0
    outputs = open('output.txt', 'w')
    outputs.write(str(ans))
    outputs.close()


if __name__ == '__main__':
    main()
