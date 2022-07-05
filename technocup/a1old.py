def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    min = 1000
    c = 0
    if n == 1:
        a[0] = input()
    elif n == 2:
        a[0], a[1] = input().split()
    elif n == 3:
        a[0], a[1], a[2] = input().split()
    elif n == 4:
        a[0], a[1], a[2], a[3] = input().split()
    elif n == 5:
        a[0], a[1], a[2], a[3], a[4] = input().split()
    elif n == 6:
        a[0], a[1], a[2], a[3], a[4], a[5] = input().split()
    elif n == 7:
        a[0], a[1], a[2], a[3], a[4], a[5], a[6] = input().split()
    elif n == 8:
        a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7] = input().split()
    elif n == 9:
        a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8] = input().split()
    if m == 1:
        b[0] = input()
    elif m == 2:
        b[0], b[1] = input().split()
    elif m == 3:
        b[0], b[1], b[2] = input().split()
    elif m == 4:
        b[0], b[1], b[2], b[3] = input().split()
    elif m == 5:
        b[0], b[1], b[2], b[3], b[4] = input().split()
    elif m == 6:
        b[0], b[1], b[2], b[3], b[4], b[5] = input().split()
    elif m == 7:
        b[0], b[1], b[2], b[3], b[4], b[5], b[6] = input().split()
    elif m == 8:
        b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7] = input().split()
    elif m == 9:
        b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8] = input().split()
    for i in range(0, n, 1):
        for j in range(0, m, 1):
            if (a[i] == b[j]):
                c = int(a[i])
            else:
                c = int(a[i] + b[j])
            if (c < min):
                min = c
    for j in range(0, m, 1):
        for i in range(0, n, 1):
            if (b[j] == a[i]):
                c = int(a[i])
            else:
                c = int(b[j] + a[i])
            if (c < min):
                min = c
    print(min)


if __name__ == '__main__':
    main()