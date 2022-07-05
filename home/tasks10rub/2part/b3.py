def main():
    a = int(input())
    if (a == 1):
        print('Monday', end='\n')
    elif (a == 2):
        print('Tuesday', end='\n')
    elif (a == 3):
        print('Wednesday', end='\n')
    elif (a == 4):
        print('Thursday', end='\n')
    elif (a == 5):
        print('Friday', end='\n')
    elif (a == 6):
        print('Saturday', end='\n')
    elif (a == 7):
        print('Sunday', end='\n')
    else:
        print('There\'s no such day')


if __name__ == '__main__':
    main()