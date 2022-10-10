import matplotlib.pyplot as plt
import numpy as np


def graph(i):
    x = np.linspace(-5, 5, 1000)
    y = list()
    y = eval(i)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    yabs_max = abs(max(ax.get_ylim(), key=abs))
    ax.set_ylim(ymin=-yabs_max, ymax=yabs_max)
    plt.plot(x, y, 'g')
    plt.savefig("graph.png")