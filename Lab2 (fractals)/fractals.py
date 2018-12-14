import numpy as np
from itertools import cycle
import matplotlib.pyplot as plt
import math
import matplotlib.colors as clr
import random


def mandelbrot_set(iterations, top_border, x_min, x_max, y_min, y_max, x_points, y_points, deg_z):
    portrait = np.zeros([x_points, y_points])

    for i, x in enumerate(np.linspace(x_min, x_max, x_points)):
        for j, y in enumerate(np.linspace(y_min, y_max, y_points)):
            c = x + 1j * y

            z = 0
            for k in range(iterations):
                z = z ** deg_z + c

                if abs(z) > top_border:
                    portrait[i, j] = k
                    break

    colorpoints = [(1 - (1 - q) ** 4, c) for q, c in zip(np.linspace(0, 1, 20), cycle(['#f85252', '#000000', '#f96400',]))]
    cmap = clr.LinearSegmentedColormap.from_list('mycmap', colorpoints, N=2048)

    fig = plt.figure()
    fig.add_subplot()
    plt.xticks([])
    plt.yticks([])
    plt.imshow(-portrait.T, cmap=cmap, interpolation='none')

    return portrait


def mandelbrot_set_trig(iterations, top_border, x_min, x_max, y_min, y_max, x_points, y_points, function):
    portrait = np.zeros([x_points, y_points])

    for i, x in enumerate(np.linspace(x_min, x_max, x_points)):
        for j, y in enumerate(np.linspace(y_min, y_max, y_points)):
            c = x + 1j * y

            z = 0
            for k in range(iterations):
                z = function(z) + c

                if abs(z) > top_border:
                    portrait[i, j] = k
                    break

    colorpoints = [(1 - (1 - q) ** 4, c) for q, c in zip(np.linspace(0, 1, 20), cycle(['#f85252', '#000000', '#f96400',]))]
    cmap = clr.LinearSegmentedColormap.from_list('mycmap', colorpoints, N=2048)

    fig = plt.figure()
    fig.add_subplot()
    plt.xticks([])
    plt.yticks([])
    plt.imshow(-portrait.T, cmap=cmap, interpolation='none')

    return portrait


def julia_set(iterations, top_border, x_min, x_max, y_min, y_max, x_points, y_points, deg_z, c_Re, c_Im):
    portrait = np.zeros([x_points, y_points])

    for i, x in enumerate(np.linspace(x_min, x_max, x_points)):
        for j, y in enumerate(np.linspace(y_min, y_max, y_points)):
            if c_Re is None and c_Im is None:
                c = random.random() + 1j * random.random()
            elif c_Re is None and c_Im is not None:
                c = random.random() + 1j * c_Im
            elif c_Im is None and c_Re is not None:
                c = c_Re + 1j * random.random()
            else:
                c = c_Re + 1j * c_Im

            z = math.cos(x) + 1j * math.cos(y)
            for k in range(iterations):
                z = z ** deg_z + c

                if abs(z) > top_border:
                    portrait[i, j] = k
                    break

    colorpoints = [(1 - (1 - q) ** 4, c) for q, c in
                   zip(np.linspace(0, 1, 20), cycle(['#f85252', '#000000', '#f96400', ]))]
    cmap = clr.LinearSegmentedColormap.from_list('mycmap', colorpoints, N=2048)

    fig = plt.figure()
    fig.add_subplot()
    plt.xticks([])
    plt.yticks([])
    plt.imshow(-portrait.T, cmap=cmap, interpolation='none')

    return portrait
