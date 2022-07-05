import math


def simple_test(z):
    flag = 0
    if (z == 2) or (z == 0):
        return True
    if z % 2 == 0:
        return False
    for i in range(3, ((math.ceil(math.sqrt(z))) + 1), 2):
        if z % i == 0:
            flag = 1
            break
    if flag == 0:
        return True
    else:
        return False


def main():
    q = int(input())
    a = []
    c = 0
    for i in range(0, q, 1):
        a.append(int(input()))
    for i in range(0, q, 1):
        count = 0
        c = a[i]
        """if simple_test(c) == True:
            print('-1')
            continue
        else:"""
        while c != 0:
            for i in range(4, c + 1, 1):
                if (simple_test(i) == False) and ((simple_test(c - i) == False) or (c - i == 0)):
                    c -= i
                    count += 1
                    break
            if (count == 0):
                break
        if (count == 0) or (c != 0):
            print('-1')
        elif (count != 0) and (c == 0):
            print(count)

if __name__ == '__main__':
    main()