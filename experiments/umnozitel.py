def umnozitel(x, y):
    print('Your number is: ', x)
    print('Your goal is: ', y)
    if x < y:
        print('-------------')
        print('1) +3')
        print('2) +4')
        print('3) +5')
        try:
            func = int(input())
            if func == 1:
                x += 3
            elif func == 2:
                x += 4
            elif func == 3:
                x += 5
            else:
                raise TypeError
        except:
            print('-------------')
            print('TRY AGAIN!!!')
            print('-------------')
            umnozitel(x, y)
        else:
            print('-------------')
            print('DONE!')
            print('-------------')
            umnozitel(x, y)
    elif x == y:
        print('-------------')
        print('Congratulations, you\'re done!!!')
        print('-------------')
    elif x > y:
        print('-------------')
        print('You lose!')
        print('-------------')

def main():
    print('-------------')
    print('Hello! It\'s umnozitel')
    print('-------------')
    a = int(input('Type your start number: '))
    b = int(input('Type your goal: '))
    print('-------------')
    umnozitel(a, b)


if __name__ == '__main__':
    main()
