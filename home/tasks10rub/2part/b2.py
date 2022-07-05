def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if (a >= b) and (a >=c):
        print(a, end='\n')
    elif (b >= a) and (a >= c):
        print(b, end='\n')
    elif (c >= a) and (c >= b):
        print(c, end='\n')


if __name__ == '__main__':
    main()