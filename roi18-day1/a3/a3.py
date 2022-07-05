def main():
    inputs = open('input.txt', 'r')
    all = inputs.read().split('\n')
    inputs.close()
    info = all[0].split(' ')
    n = int(info[0])
    m = int(info[1])
    del info
    sotrudniki_beta = []
    # sotrudniki = []
    # presod = []
    info1 = []
    # not_found = True
    min_time = 10 ** 9 + 1
    min_floor = 10 ** 9 + 1
    for i in range(0, n, 1):
        info = all[1 + i].split()
        info1.append(int(info[0]))
        info1.append(int(info[1]))
        sotrudniki_beta.append(info1)
        del info
        info1 = []

    # Sorting. Function, on which I waste my f*ckng time
    """while not_found:
        for i in range(0, n, 1):
            if sotrudniki_beta[i] in sotrudniki:
                continue
            if (sotrudniki_beta[i][0] < min_time):
                min_time = sotrudniki_beta[i][0]
            if sotrudniki_beta[i][0] == min_time:
                if sotrudniki_beta[i][1] < min_floor:
                    min_floor = sotrudniki_beta[i][1]
        presod.append(min_time)
        presod.append(min_floor - 1)
        sotrudniki.append(presod)
        presod = []
        min_time = 10 ** 9 + 1
        min_floor = 10 ** 9 + 1
        if len(sotrudniki_beta) == len(sotrudniki):
            not_found = False"""

    # Deleting variables
    # del presod
    # del sotrudniki_beta
    del min_time
    del min_floor
    del info1

    # Initializing new vars
    current_state = 0
    time = 0
    in_elevator = 0
    in_time = False
    uechali = []
    uechali_index = []
    sotrudniki_time = []
    for i in range(0, len(sotrudniki_beta), 1):
        sotrudniki_time.append(0)
    who = 0
    kolvo = []
    max_floor = 1
    min_time = 10 ** 9 + 1

    # Main action
    while True:
        if sotrudniki_time.count(0) == 0:
            break
        for i in range(len(sotrudniki_beta)):
            if (time >= sotrudniki_beta[i][0]) and (sotrudniki_beta[i] not in uechali):
                in_time = True
                who = sotrudniki_beta[i][1] - 1
                break
            else:
                in_time = False
                if (sotrudniki_beta[i][0] < min_time) and (sotrudniki_beta[i] not in uechali):
                    min_time = sotrudniki_beta[i][0]
        if in_time:
            time += abs(who - current_state)
            current_state = who
            for i in range(len(sotrudniki_beta)):
                if (current_state == sotrudniki_beta[i][1] - 1) and (sotrudniki_beta[i][0] <= time) and (sotrudniki_beta[i] not in uechali):
                    kolvo.append(i)
            if len(kolvo) != 0:
                in_elevator += len(kolvo)
                for i in range(len(kolvo)):
                    uechali.append(sotrudniki_beta[kolvo[i]])
                    uechali_index.append(kolvo[i])
                kolvo = []
        else:
            time += min_time
            min_time = 10 ** 9 + 1
        if in_elevator:
            while (current_state != 1):
                for i in range(len(sotrudniki_beta)):
                    if sotrudniki_beta[i][1] - 1 < current_state and sotrudniki_beta[i][1] - 1 > max_floor - 1 and sotrudniki_beta[i][0] < time + current_state and sotrudniki_beta[i] not in uechali:
                        max_floor = sotrudniki_beta[i][1] - 1
                time += (current_state - max_floor)
                current_state -= (current_state - max_floor)
                max_floor = 1
                """current_state -= 1
                time += 1"""
                for i in range(len(sotrudniki_beta)):
                    if (current_state == sotrudniki_beta[i][1] - 1) and (sotrudniki_beta[i][0] <= time) and (sotrudniki_beta[i] not in uechali):
                        kolvo.append(i)
                if len(kolvo) != 0:
                    in_elevator += len(kolvo)
                    for i in range(len(kolvo)):
                        uechali.append(sotrudniki_beta[kolvo[i]])
                        uechali_index.append(kolvo[i])
                    kolvo = []
            current_state -= 1
            time += 1
            in_elevator = 0
            for i in range(0, len(uechali_index), 1):
                sotrudniki_time[uechali_index[i]] = time
            uechali_index = []

    # Output
    outputs = open('output.txt', 'w')
    for i in range(len(sotrudniki_time)):
        outputs.write(str(sotrudniki_time[i]) + '\n')
    outputs.close()


if __name__ == '__main__':
    main()
