from perfect_numbers1 import main
import threading


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        main()

th = MyThread()
th.start()
th.join()