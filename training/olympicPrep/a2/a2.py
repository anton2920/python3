def main():
    inputs = open('input.txt', 'r')
    all = inputs.read().split()
    print(all)
    n = int(all[0])
    m = int(all[1])
    k = int(all[2])
    inputs.close()
    t = []
    a = []
    for i in range(0, k, 1):
        t.append(int(all[3 + i]))
    for i in range(0, n, 1):
        a.append(i)
    for i in range(0, k, 1):
        a.insert(0, a.pop(t[i] % n))
    ans = a.index(m - 1) + 1
    outputs = open('output.txt', 'w')
    outputs.write(str(ans))


if __name__ == '__main__':
    main()