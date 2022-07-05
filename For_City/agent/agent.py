def tik(x1, y1, x2, y2, x3, y3, x4, y4):
    common = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if common == 0.0:
        return False
    rh = (y1 - y3) * (x4 - x3) - (x1 - x3) * (y4 - y3)
    sh = (y1 - y3) * (x2 - x1) - (x1 - x3) * (y2 - y1)

    r = rh / common
    s = sh / common

    if ((r >= 0) and (r <= 1) and (s >= 0) and (s <= 1)):
        return True
    else:
        return False


def main():
    a = []
    b = []
    inputs = open('agent.in', 'r')
    a = inputs.read().split()
    inputs.close()
    for i in range(0, len(a), 1):
        b.append(float(a[i]))
    print(a)
    print(b)
    del(a)
    agent = [b[0], b[1]]
    spy = [b[2], b[3]]
    x = 0.0
    y = 0.0
    n = int(b[4])
    c = []
    for i in range(0, 4 * n, 1):
        c.append(b[5 + i])
    print(c)
    k = 0
    del b
    outputs = open('agent.out', 'w')
    for i in range(1, n + 1, 1):
        xlu = c[0 + k]
        ylu = c[1 + k]
        xrd = c[2 + k]
        yrd = c[3 + k]
        xld = xlu
        yld = yrd
        xru = xrd
        yru = ylu
        if (tik(agent[0], agent[1], spy[0], spy[1], xlu, ylu, xru, yru)) or (tik(agent[0], agent[1], spy[0], spy[1], xlu, ylu, xld, yld)) or (tik(agent[0], agent[1], spy[0], spy[1], xru, yru, xrd, yrd)) or (tik(agent[0], agent[1], spy[0], spy[1], xld, yld, xrd, yrd)):
            outputs.write(str(i))
            outputs.close()
            return 0
        k += 4
    outputs.write('yes')


if __name__ == '__main__':
    main()
