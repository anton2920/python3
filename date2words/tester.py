import os


def main():
    if os.path.exists('output.txt'):
        os.remove('output.txt')
    for month in range(1, 13):
        for day in range(1, 32):
            os.system('/bin/bash /home/anton/C/lab/lab_dev/lab_04.bash 2020-{month}-{day} >> output.txt'.format(
                month=str(month),
                day=str(day)))


if __name__ == '__main__':
    main()
