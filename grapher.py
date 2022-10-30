import matplotlib.pyplot as plt
import numpy


def graph(i):
    dim = 10
    x = numpy.linspace(-5, 5, 10)
    y = eval(i)
    print(type(y))
    if type(y) is tuple:
        y = list(y)
    if type(y) is not list:
        if not type(x) == type(y) or not len(x) == len(y):
            y = tuple([y for _ in range(len(x))])
    else:
        for elem_index in range(len(y)):
            if type(y[elem_index]) in (float, int) or not len(x) == len(y[elem_index]):
                y[elem_index] = [y[elem_index] for _ in range(len(x))]
    print(y)
    print(x)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    y_abs_max = dim
    ax.set_ylim(ymin=-y_abs_max, ymax=y_abs_max)
    x_abs_max = dim
    ax.set_xlim(xmin=-x_abs_max, xmax=x_abs_max)
    if type(y) is list:
        for graph_y in y:
            plt.plot(x, graph_y, 'g')
    else:
        plt.plot(x, y, 'g')
    ax.set_aspect(1)
    plt.savefig("graph.png")
