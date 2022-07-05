import math
import time
# import pp
# import random


def func(x):
    return (2 ** (x - 1)) * ((2 ** x) - 1)


'''def simple(y, y1):
    flag1 = 0
    sch3 = 0
    for sch1 in range(3, y1 + 1, 1):
        sch3 += 1
        for sch2 in range(2, ((sch1 // 2) + 1), 1):
            if sch1 % sch2 == 0:
                flag1 == 1
                break
        if (sch3 == y) and (flag1 == 0):
            return sch1  '''


def simple_test(z):
    a = ((2 ** z) - 1)
    flag = 0
    if a % 2 == 0:
        return False
    for i in range(3, ((math.ceil(math.sqrt(a))) + 1), 2):
        if a % i == 0:
            flag = 1
            break
    if flag == 0:
        return True
    else:
        return False

        #Old method


'''def simple_test(z):
    p = ((2 ** z) - 1)
    if p % 2 == 0:
        return False
    a = 2
    if a % p != 0:
        b = ((a ** (p - 1)) - 1)
        if b % p == 0:
            return True
        else:
            return False
    else:
        return False

        # New Method (Fermat's little theorem)
'''


def main():
    a = 0
    n = 1
    t1 = time.time()
    while True:
        n += 1
        if simple_test(n) == True:
            a = func(n)
            print(a, ' Time is ', time.time() - t1, end='\n')


if __name__ == '__main__':
    print('Perfect numbers: ')
    main()