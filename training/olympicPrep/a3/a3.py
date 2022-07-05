def main():
    inputs = open('input.txt', 'r')
    all = inputs.read().split('\n')
    a = all[0].split(':')
    b = all[1].split(':')
    c = all[2].split(':')
    inputs.close()
    ans = []
    delta = []
    if int(c[0]) < int(a[0]):
        a[0] = str(24 - int(a[0]))
    for i in range(3):
        delta.append(abs(int(c[i]) - int(a[i])))
    delta[0] = int(c[0]) + delta[0]
    sec = delta[0] * 3600 + delta[1] * 60 + delta[2]
    if sec / 2 != int(sec / 2):
        sec = round((sec + 0,1) / 2)
    else:
        sec = round(sec / 2)
    b1 = int(b[0]) * 3600 + int(b[1]) * 60 + int(b[2])
    ans1 = b1 + sec
    if ans1 // 3600 < 10:
        ans.append('0' + str(ans1 // 3600))
    else:
        ans.append(str(ans1 // 3600))
    ans1 = ans1 % 3600
    if ans1 // 60 < 10:
        ans.append('0' + str(ans1 // 60))
    else:
        ans.append(str(ans1 // 60))
    ans1 = ans1 % 60
    if ans1 < 10:
        ans.append('0' + str(ans1))
    else:
        ans.append(str(ans1))
    if int(ans[0]) > 24:
        ans[0] = str(int(ans[0]) - 24)
    if int(ans[0]) % 10 == 0:
        ans[0] = '0' + ans[0]
    outputs = open('output.txt', 'w')
    outputs.write(ans[0] + ':' + ans[1] + ':' + ans[2])
    outputs.close()


if __name__ == '__main__':
    main()