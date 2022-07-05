def main():
    inputs = open('input.txt', 'r')
    all = inputs.read().split()
    a = int(all[0])
    b = int(all[1])
    k = int(all[2])
    inputs.close()
    leftx = round(a ** (1 / 2))
    rightx = round(b ** (1 / 2))
    lefty = round(a ** (1 / 3))
    righty = round(b ** (1 / 3))
    ans = 0
    for x in range(leftx, rightx + 1, 1):
        for y in range(lefty, righty + 1, 1):
            if (a <= x ** 2 <= b) and (abs(x ** 2 - y ** 3) <= k) and (a <= y ** 3 <= b):
                ans += 1
    outputs = open('output.txt', 'w')
    outputs.write(str(ans))
    outputs.close()


if __name__ == '__main__':
    main()
