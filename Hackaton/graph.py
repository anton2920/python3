from numpy import *
import scipy
import matplotlib.pyplot as plt
import matplotlib as mpl


def count(func, x):
    """xa = []
    ya = []
    ymax = -32767
    x = int(xmin)
    func = str(func)
    while True:
        try:
            ya.append(eval(func))
            y = eval(func)
            if y > ymax:
                ymax = y
        except (SyntaxError):
            break
        except (ZeroDivisionError):
            x += 0.01
            continue
        xa.append(x)
        x += 0.1
        if int(x) == int(xmax):
            break"""
    x = int(x)
    try:
        a = eval(func)
    except (SyntaxError):
        return 'buy'
    except (ZeroDivisionError):
        return 'zero'
    else:
        return a


"""def main(func, xmin, xmax, color, thickness):
    sty = ''
    count(func, xmin, xmax)
    plt.plot(xa, ya, color=color, linewidth=float(thickness))
    plt.ylabel(func)
    plt.show()"""


"""def demo(sty):
    mpl.style.use(sty)
    fig, ax = plt.subplots(figsize=(3, 3))

    ax.set_title('style: {!r}'.format(sty), color='C0')

    ax.plot(th, cos(th), 'C1', label='C1')
    ax.plot(th, sin(th), 'C2', label='C2')
    ax.legend()
    plt.show()"""

if __name__ == '__main__':
    pass
    """th = linspace(0, 2 * pi, 128)
    demo('default')
    demo('seaborn')"""
