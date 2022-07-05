def count1(x):
    return x.count('1')


def main():
    a = input()
    i = int(a[0]) + int(a[1])
    j = int(a[3]) + int(a[4])
    k = int(a[2])
    if (i > 9):
        b = str(i)
        i = int(b[0]) + int(b[1])
    if (j > 9):
        b = str(i)
        j = int(b[0]) + int(b[1])
    if ((i == j) and (i == k) and (j == k)) or ((count1(bin(i)) == count1(bin(j))) and (count1(bin(i)) == count1(bin(k))) and (count1(bin(j)) == count1(bin(k)))):
        print('It\'s a lucky ticket', end='\n')
    else:
        print('It\'s not a lucky ticket', end='\n')


if __name__ == '__main__':
    main()