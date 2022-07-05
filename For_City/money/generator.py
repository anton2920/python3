from random import randint


def main():
    outputs = open('money.in', 'w')
    for i in range(1000000):
        outputs.write('\n' + str(randint(999999980, 1000000000)))
    outputs.close()

if __name__ == '__main__':
    main()