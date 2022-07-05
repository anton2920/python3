import math


def is_simple(x):
    f = True
    if x % 2 == 0:
        return False
    else:
        for i in range(3, math.ceil(math.sqrt(x)), 2):
            if x % i == 0:
                f = False
                break
        if f == False:
            return False
        else:
            return True

def is_amorph(x):
    x1 = x
    k = 1
    while x1 > 0:
        x1 = x1 // 10
        k *= 10
    if ((x*x) % k == x):
        return True
    else:
        return False


def is_poly(x):
    x1 = x
    k = 0
    while x1 > 0:
        k *= 10
        k += x1 % 10
        x1 = x1 // 10
    if k == x:
        return True
    else:
        return False

def main():
    k1 = 0
    k2 = 0
    k3 = 0
    a = []
    b = []
    b1 = []
    b2 = []
    b3 = []
    for i in range(3):
        for j in range(5):
           b.append(0)
        a.append(b)
        b = []
    for i in range (100, 10001, 1):
        if is_simple(i) == True:
            if k1 <= 5:
                b1.append(i)
                k1 += 1
        if is_poly(i) == True:
            if k2 <= 5:
                b2.append(i)
                k2 += 1
        if is_amorph(i) == True:
            if k3 <= 5:
                b3.append(i)
                k3 += 1
        if (k1 == 6) and (k2 == 6) and (k3 == 6):
            break;
    a = []
    a.append(b1)
    a.append(b2)
    a.append(b3)
    for i in range(2):
        b3.append(0)
    for i in range(3):
        for j in range(5):
            print(a[i][j], end=' ')
        print('\n')
if __name__ == '__main__':
    main()