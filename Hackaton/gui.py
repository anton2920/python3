import graph
import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master)
        self.master.title('Hello, World!')

        self.myLab = tk.Label(self.master, text='Region - 32. Ultimate graph painter').pack()

        self.btn_quit = tk.Button(self.frame, text='Quit', width=25, command=self.click_quit).pack(side='right')
        self.btn_cus = tk.Button(self.frame, text='Custom', width=25, command=self.click_cus).pack(side='right')
        self.btn_def = tk.Button(self.frame, text='Default', width=25, command=self.new_window).pack(side='right')

        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddWin(self.newWindow)

    def click_quit(self):
        print('Cancel')
        self.master.destroy()

    def click_cus(self):
        print('Cancel')
        self.master.destroy()


class AddWin:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master)
        self.funcs = ['sin(x)', 'cos(x)', 'x * x']
        self.list1 = tk.Listbox(self.frame)
        for i in self.funcs:
            self.list1.insert('end', i)
        self.list1.pack(side='left')

        self.a = tk.StringVar()
        self.b = tk.StringVar()
        self.c = tk.StringVar()
        self.xmin = tk.StringVar()
        self.xmax = tk.StringVar()
        self.is_on = tk.IntVar()

        self.cbtn1 = tk.Checkbutton(self.frame, text='Turn on the coefficients', command=self.coef, variable=self.is_on).pack()

        self.frame.pack()

        self.aLab = tk.Label(self.frame, text='a = ')
        self.aC = tk.Entry(self.frame, textvariable=self.a)

        self.bLab = tk.Label(self.frame, text='b = ')
        self.bC = tk.Entry(self.frame, textvariable=self.b)

        self.cLab = tk.Label(self.frame, text='c = ')
        self.cC = tk.Entry(self.frame, textvariable=self.c)

        self.xminE = tk.Entry(self.frame, textvariable=self.xmin).pack(side='bottom')
        self.xminL = tk.Label(self.frame, text='Xmin = ').pack(side='bottom')

        self.xmaxE = tk.Entry(self.frame, textvariable=self.xmax).pack(side='bottom')
        self.xmaxL = tk.Label(self.frame, text='Xmax = ').pack(side='bottom')

    def coef(self):
        if self.is_on.get() == 1:
            self.aLab.pack()
            self.aC.pack()

            self.bLab.pack()
            self.bC.pack()

            self.cLab.pack()
            self.cC.pack()
        else:
            self.aLab.pack_forget()
            self.aC.pack_forget()

            self.bLab.pack_forget()
            self.bC.pack_forget()

            self.cLab.pack_forget()
            self.cC.pack_forget()



def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    pass