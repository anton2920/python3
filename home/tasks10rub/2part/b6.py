def main():
    a = int(input())
    b = bin(a)
    b = b[2::]
    b1 = b[::-1]
    if (b == b1):
        print('It\'s a palindrome', end='\n')
    else:
        print('It\'s not a palindrome', end='\n')


if __name__ == '__main__':
    main()
