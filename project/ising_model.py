"""
I used multiple sources from GitHub shown below that I used to assist me in creating the Ising model
The original code did not have comments so I made some based on my current knowledge but  
"""
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


def monte_carlo_move(config, N, beta):
    ''' This is to execute the monte carlo moves using
    Metropolis algorithm such that detailed
    balance condition is satisified'''
    for i in range(N):
        for j in range(N):
            a = np.random.randint(0, N)
            b = np.random.randint(0, N)
            s = config[a, b]
            nb = config[(a + 1) % N, b] + config[a, (b + 1) % N] + config[(a - 1) % N, b] + config[a, (b - 1) % N]
            cost = 2 * s * nb
            if cost < 0:
                s *= -1
            elif rand.random() < np.exp(-cost * beta):
                s *= -1
            config[a, b] = s
    return config


def configPlot(f, config, i, N, n_):
    """ This module plots the configuration once passed to it along with time etc """

    X, Y = np.meshgrid(range(N), range(N))
    sp = f.add_subplot(3, 3, n_)
    plt.setp(sp.get_yticklabels(), visible=False)
    plt.setp(sp.get_xticklabels(), visible=False)
    plt.pcolormesh(X, Y, config, cmap=plt.cm.RdBu)
    plt.title('Time=%d' % i)
    plt.axis('tight')
    plt.show()


def simulate():
    # Choose NxN grid points and Temperature
    N, temp = 100, 20
    # Create 100x 100
    config = 2 * np.random.randint(2, size=(N, N)) - 1
    f = plt.figure(figsize=(15, 15), dpi=80)
    configPlot(f, config, 0, N, 1)

    msrmnt = 1001
    for i in range(msrmnt):
        monte_carlo_move(config, N, 1.0 / temp)
        if i == 1:
            configPlot(f, config, i, N, 2)
        if i == 4:
            configPlot(f, config, i, N, 3)
        if i == 32:
            configPlot(f, config, i, N, 4)
        if i == 100:
            configPlot(f, config, i, N, 5)
        if i == 1000:
            configPlot(f, config, i, N, 6)
N=simulate()
