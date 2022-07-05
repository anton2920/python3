def sred(x, y, z, t):
    return (2 * x + 3 * y + 4 * z + 5 * t) / (x + y + z + t)


def main():
    inputs = open('input.txt', 'r')
    all = inputs.read().split()
    a = int(all[0])
    b = int(all[1])
    c = int(all[2])
    inputs.close()
    ocenki = []
    ans = 0
    d = 0
    not_four = True
    while not_four:
        if round(sred(a, b, c, d)) != 4:
            d += 1
        else:
            not_four = False
    outputs = open('output.txt', 'w')
    outputs.write(str(d))
    outputs.close()


if __name__ == '__main__':
    main()