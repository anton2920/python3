def main():

    # Initializing variables
    a = int(input())
    b = a
    o = b % 10
    b = int(b / 10)
    t = b % 10
    b = int(b / 10)
    h = b % 10
    b = int(b / 10)

    # Main part
    a = b * 1000 + t * 100 + o * 10 + h

    # Final output
    print(a)


if __name__ == '__main__':
    main()