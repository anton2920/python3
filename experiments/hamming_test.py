def hamming(msg):
    check = ''
    check1 = int(msg[0]) ^ int(msg[1]) ^ int(msg[2])
    check2 = int(msg[1]) ^ int(msg[2]) ^ int(msg[3])
    check3 = int(msg[0]) ^ int(msg[1]) ^ int(msg[3])
    check = str(check1) + str(check2) + str(check3)
    return msg + check

def hamming2(msg):
    check3 = int(msg[3]) ^ int(msg[2]) ^ int(msg[1])
    check2 = int(msg[3]) ^ int(msg[2]) ^ int(msg[0])
    check1 = int(msg[3]) ^ int(msg[1]) ^ int(msg[0])
    return str(check1) + str(check2) + str(msg[0]) + str(check3) + msg[1::]


def zeroes(should, codes):
    new_codes = []
    for i in codes:
        new_codes.append('0' * (should - len(i)) + i)
    return new_codes


def combinate(codes, bin4, file_name):
    all_matricies = []
    total_count = 0
    flag = False
    for x in codes:
        for y in codes:
            for z in codes:
                for t in codes:
                    if (x == y == z == t):
                        continue
                    if (int(x) == 0 or int(y) == 0 or int(z) == 0 or int(t) == 0):
                        continue
                    for coef in bin4:
                        if (int(coef) == 0):
                            continue
                        if ((int(coef[0]) * int(x)) ^ (int(coef[1]) * int(y)) ^ (int(coef[2]) * int(z)) ^ (int(coef[3]) * int(t)) == 0):
                            flag = True
                            continue
                    if (flag == False):
                        total_count += 1
                        matrix = []
                        matrix.append(x)
                        matrix.append(y)
                        matrix.append(z)
                        matrix.append(t)
                        all_matricies.append(matrix)
                    flag = False
    print(total_count)
    print_em_all(all_matricies, file_name)


def print_em_all(matrix, file_name):
    fp = open(file_name, 'w')
    if not fp.closed:
        for m in matrix:
            for row in m:
                fp.write(row + '\n')
            fp.write('\n')

        fp.close()


def main():
    bin4 = []
    codes = []
    codes2 = []
    for i in range(16):
        bin4.append(bin(i)[2::])
    bin4 = zeroes(4, bin4)
    print(bin4)
    for i in bin4:
        codes.append(hamming(i))
        codes2.append(hamming2(i))
    codes = zeroes(7, codes)
    codes2 = zeroes(7, codes2)
    print(codes)
    print(codes2)

    # Linear indepenndance
    combinate(codes, bin4, 'matrix.txt') # (7,4)-code
    combinate(codes2, bin4, 'matrix2.txt') # Hamming from Hamming himself


if __name__ == '__main__':
    main()
