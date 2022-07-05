import tkinter as tk
import graph

class Main:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, width = 500, height = 500)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddWin(self.newWindow)

class AddWin:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        value = tk.StringVar(self.master)
        value.set("function")
        w = tk.OptionMenu(self.master, value, "sin", "cos", "tan", "x²")
        w.pack()

        self.graphButton = tk.Button(self.frame, text = "Plot", width = 25, command = self.plot)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)

        self.graphButton.pack()
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

    def plot(self):
        va = value.get()
        if va == 'sin' or va == 'cos' or va == 'tan':
            va = va + '(x)'
        if va == 'x²':
            va = 'x * x'
        graph.main(va)

def main():
    root = tk.Tk()
    app = Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()