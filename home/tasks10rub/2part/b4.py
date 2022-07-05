def main():
    a1 = input()
    a2 = a1[::-1]
    if (a2 == a1):
        print('It\'s a palindrome', end='\n')
    else:
        print('It\'s not a palindrome', end='\n')


if __name__ == '__main__':
    main()