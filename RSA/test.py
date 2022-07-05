import multiprocessing

def run():
    global c
    x = c * c
    save(x)


if __name__ == '__main__':
    c = 3173056089455875209020892579757
    for i in range (7000904390028420840687967141889):
        p = multiprocessing.Process(target=run)
        p.start()
