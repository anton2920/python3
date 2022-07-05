def main():
    a = []
    b = []
    a.append(input().split())
    for i in range(0, 6, 1):
        b.append(int(a[0][i]))
    max = 5
    for i in range(0, 6, 1):
        for j in range(0, 6, 1):
            for k in range(0, 6, 1):
                if ((b[i] + b[j] + b[k]) == (b[max - i] + b[max - j] + b[max - k])) and ((i != j) and (i != k) and (j != k) and (max - i != i) and (max - j != i) and (max - k != i) and (max - i != j) and (max - j != j) and (max - k != j) and (max - i != k) and (max - j != k) and (max - k != k)):
                    print('YES', end='\n')
                    return 0
                else:
                    flag = False

    if flag == False:
        print('NO', end='\n')
        return 0


if __name__ == '__main__':
    main()