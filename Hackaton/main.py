import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import colors
from numpy import *


def main():
    inputs = open('/home/anton/PABC/home/HackatonGUI/ForPY.txt', 'r')
    a = []
    b = []
    c = []
    yaa = []
    xaa = []
    x0 = []
    y0 =[]
    func = ''
    clr = 'black'
    ymaxa = -1000000
    xmaxa = -1000000
    ymina = 1000000
    xmina = 1000000
    a = inputs.read().split('\n')
    print(a)
    for i in range (0, len(a), 1):
        b = a[i].split(':')
        c.append(b)
        b = []
    print(c)
    inputs.close()
    j = 0
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(0, len(c) - 2, 1):
        xa = []
        ya = []
        ymax = -1000000
        xmax = -1000000
        ymin = 1000000
        xmin = 1000000
        xikikmax = 0.0
        xikikmin = 0.0
        j += 1
        x = float(c[i][1])
        while int(x) != int(c[i][2]):
            try:
                d = eval(c[i][0])
                if ((('/ x' in c[i][0]) or ('tan' in c[i][0])) and round(x, 2) == 0):
                    raise ZeroDivisionError
            except (SyntaxError):
                return 0
            except (ZeroDivisionError):
                x += 0.001
                continue
            else:
                if d > ymax:
                    ymax = d
                    xikikmax = x
                if d < ymin:
                    ymin = d
                    xikikmin = x
                if x < xmin:
                    xmin = x
                    fincmin = d
                if x > xmax:
                    xmax = x
                    fincmax = d
                if round(x, 2) == 0.00:
                    x0.append(x)
                xa.append(x)
                ya.append(d)
                x += 0.001
            if round(d, 2) == 0.00:
                y0.append(x)
        if c[len(c) - 2][5] == '1':
            ax.scatter(xikikmin, ymin, edgecolors=clr, s=90)
            ax.scatter(xikikmax, ymax, edgecolors=clr, s=90)
        if ymax > ymaxa:
            ymaxa = ymax
        if ymin < ymina:
            ymina = ymin
        if xmax > xmaxa:
            xmaxa = xmax
        if xmin < xmina:
            xmina = xmin
        xaa.append(xa)
        yaa.append(ya)
        ax.plot(xaa[i], yaa[i], label=c[i][0], color=c[i][3], linewidth=float(c[i][4]))
    if c[j][0] == '#000000':
        clr = 'white'
    if c[j][1] == '1':
        ax.plot([0, 0, 0], [ymina, 0, ymaxa], color=clr)
        ax.plot([xmina, 0, xmaxa], [0, 0, 0], color=clr)
        if c[j][3] == '1':
            for i in range(0, len(c) - 2, 1):
                func = c[i][0]
                for x in x0:
                    ax.scatter(0, eval(func), edgecolors=clr, s=50)
                for m in y0:
                    ax.scatter(m, 0, edgecolors=clr, s=50)
    ax.patch.set_facecolor(colors.hex2color(c[j][0]))
    if c[j][2] == '1':
        ax.grid(color=clr, linestyle='--', linewidth='1')
    if c[j][4] == '1':
        for i in range(0, len(c) - 2, 1):
            for k in range(0, len(c) - 2, 1):
                if i == k:
                    continue
                for x in xaa[i]:
                    if round(eval(c[i][0]), 2) == round(eval(c[k][0]), 2):
                        ax.scatter(x, eval(c[i][0]), edgecolors=clr, s=20)
    if c[j + 1][0] == '1':
        x = int(c[j + 1][2])
        d = int(c[j + 1][1])
        ax.scatter(x, eval(c[d][0]), edgecolors=clr, s=120)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
