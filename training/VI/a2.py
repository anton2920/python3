def main():

    # Initializing variables
    k = 0
    b = []

    # Main part
    while 1:
        a = input()

        if a[0] == 'А' and k <= 5 and a not in b:
            k += 1
            b.append(a)

        if k < 5:
            print('ещё')
        elif k == 5:
            print('всё!')
            exit(0)  # Idk
        else:
            pass


if __name__ == '__main__':
    main()