def main():
    a = []
    inputs = open('building.in', 'r')
    a = inputs.read().split('\n')
    print(a)
    b = []
    for i in range(0, len(a), 1):
        b.append(a[i].split())
    print(b)


if __name__ == '__main__':
    main()