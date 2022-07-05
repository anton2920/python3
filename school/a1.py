import numpy as np


def main():
    a = []
    n = int(input())
    max = -1
    for i in range(0, n, 1):
        a.append(int(input()))
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if (a[i] * a[j] > max) and (np.abs(i - j) >= 8):
                max = a[i] * a[j]
            else:
                continue
    print(max, end='\n')


if __name__ == '__main__':
    main()