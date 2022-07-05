def f(x):
    def f1(y):
        cit = []
        if
        return cit
    for i in range(1, len(x), 1):
        if x[i] != 0 and x[0] != i:
            f1(x)
            f(roads[i - 1])
    return 0


def main():
    global city
    city = []
    a = []
    b = []
    inputs = open('roads.in', 'r')
    a = inputs.read().split()
    inputs.close()
    for i in range(0, len(a), 1):
        b.append(int(a[i]))
    print(a)
    print(b)
    del(a)
    n = b[0]
    global roads
    roads = []
    roads1 = []
    for i in range(0, n, 1):
        roads1.append(i + 1)
        for j in range(0, n, 1):
            roads1.append(0)
        roads.append(roads1)
        roads1 = []
        print(roads[i], end='\n')
    m = b[1]
    k = 0
    counter = 0
    for i in range(0, m, 1):
        x = b[2 + k] - 1
        y = b[3 + k]
        roads[x][y] = b[4 + k]
        roads[y - 1][x + 1] = b[4 + k]
        k += 3
    print(roads)
    for road in roads:
        if f(road) != True:
            counter += 1


if __name__ == '__main__':
    main()