def main():
    inputs = open('input.txt', 'r')
    all = inputs.read().split('\n')
    k = int(all[0])
    n = int(all[1])
    a = []
    current_state = -1
    total_time = 0
    mnozitel = 1
    in_elevator = 0
    vsego = 0
    dovezeno = 0
    for i in range(n):
        a.append(int(all[2 + i]))
        vsego += a[i]
    inputs.close()
    while True:
        if (in_elevator == k):
            total_time += current_state + 1
            current_state = -2
        if current_state == n - 1:
            current_state = -2
            total_time += n - 1
        current_state += mnozitel
        if current_state == -1:
            mnozitel = 1
            current_state += mnozitel
            dovezeno += in_elevator
            in_elevator = 0
            if dovezeno == vsego:
                break
        total_time += 1
        if a[current_state] != 0:
            for i in range(0, a[current_state], 1):
                if in_elevator < k:
                    a[current_state] -= 1
                    in_elevator += 1
                else:
                    break

    outputs = open('output.txt', 'w')
    outputs.write(str(total_time))
    outputs.close()


if __name__ == '__main__':
    main()