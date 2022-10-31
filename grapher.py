import matplotlib.pyplot as plt
import numpy as np
import builtins
import math
from random import randint


def graph(points, bounds, domain, imports, func):
    d = tuple(map(float, eval(domain)))
    x = np.linspace(d[0], d[1], points)
    func_list = func.split(";")
    if len(imports) > 0:
        for name in imports:
            elems = name.split(".")
            print(elems)
            if len(elems) == 1:
                if len(elems[0]) > 0:
                    globals()["b_"+elems[0]] = np.vectorize(getattr(builtins, elems[0]))
            else:
                element = getattr(globals()[elems[0]], elems[1])
                globals()[elems[1]] = np.vectorize(element) if callable(element) else element
    for i in range(len(func_list)):
        func_list[i] = func_list[i].strip()
    y = []
    for elem in func_list:
        y.append(eval(elem))
    if type(y) is tuple:
        y = list(y)
    if type(y) is not list:
        if not type(x) == type(y) or not len(x) == len(y):
            y = tuple([y for _ in range(len(x))])
    else:
        for elem_index in range(len(y)):
            if type(y[elem_index]) in (float, int, np.float64) or not len(x) == len(y[elem_index]):
                y[elem_index] = [y[elem_index] for _ in range(len(x))]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    y_abs_max = bounds
    ax.set_ylim(ymin=-y_abs_max, ymax=y_abs_max)
    x_abs_max = bounds
    ax.set_xlim(xmin=-x_abs_max, xmax=x_abs_max)
    if type(y) is list:
        for i in range(len(y)):
            plt.plot(x, y[i], color=get_colour(), label=func_list[i])
    else:
        plt.plot(x, y, 'g', label=func)
    plt.legend(loc="upper left")
    ax.set_aspect(1)
    ax.set_xlabel("x")
    ax.xaxis.set_label_coords(1, 0.55)
    ax.set_ylabel("y", rotation="horizontal")
    ax.yaxis.set_label_coords(0.525, 1)
    y_ticks = ax.get_yticks()
    y_ticks = y_ticks[y_ticks != 0.0]
    ax.set_yticks(y_ticks)
    plt.savefig("graph.png")


def get_colour():
    r = str("{0:x}".format(randint(0, 255)))
    g = str("{0:x}".format(randint(0, 255)))
    b = str("{0:x}".format(randint(0, 255)))
    if len(r) == 1:
        r = "0" + r[0]
    elif len(r) == 0:
        r = "00"
    if len(g) == 1:
        g = "0" + g[0]
    elif len(g) == 0:
        g = "00"
    if len(b) == 1:
        b = "0" + b[0]
    elif len(b) == 0:
        b = "00"
    return f"#{r}{g}{b}"
