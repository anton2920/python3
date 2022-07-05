def find_p(x, y):
    global a
    global count
    if x < 0 or x > 5 or y < 0 or y > 5:
        return 0
    if a[y][x] == 'F':
        return 1
    if a[y][x] != '.' and a[y][x] != 'S':
        return 0
    a[y][x] = '+'
    count += 1
    if find_p(x, y - 1):
        return 1
    if find_p(x + 1, y):
        return 1
    if find_p(x, y + 1):
        return 1
    if find_p(x - 1, y):
        return 1
    a[y][x] = 'x'
    return 0


def main():
    global a
    global count
    count = 0
    a = [['S', '.', '.', '.', '#', '#'], ['#', '.', '#', '.', '.', '.'], ['.', '.', '#', '.', '.', '#'], ['.', '.', '#', '#', '#', '.'], ['#', '.', '.', '.', '#', '#'], ['#', '#', '#', '.', '.', 'F']]
    find_p(0, 0)
    print(count)


if __name__ == '__main__':
    main()
