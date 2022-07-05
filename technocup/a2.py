def main():
    a = []
    b = []
    c = []
    n = int(input())
    a.append(input().split())
    for i in range(0, n, 1):
        b.append(int(a[0][i]))
        c.append(int(a[0][i]))
    for i in range(0, n, 1):
        try:
            while(True):
                c.remove(b[i])
        except:
            pass


    print(c[0], end='\n')


if __name__ == '__main__':
    main()