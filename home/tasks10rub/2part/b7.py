def main():
    a = float(input())
    b = float(input())
    c = float(input())
    d = (b ** 2) - (4 * a * c)
    if ((d > 0) or (d < 0)):
        x1 = ((b * (-1)) + d ** 0.5) / (2 * a)
        x2 = ((b * (-1)) - d ** 0.5)/ (2 * a)
        print(x1, x2, sep=' ', end='\n')
    elif (d == 0):
        x1 = ((b * (-1)) + d ** 0.5) / (2 * a)
        print(x1, end='\n')


if __name__ == '__main__':
    main()