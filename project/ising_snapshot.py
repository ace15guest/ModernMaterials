import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

from numpy.random import rand

from scipy.sparse import spdiags, linalg, eye


class Ising():
    ''' Simulating the Ising model '''
    def __init__(self):
        self.avg_spin = [0]

    ## monte carlo moves
    def mcmove(self, config, N, beta, J=1.):
        ''' This is to execute the monte carlo moves using
        Metropolis algorithm such that detailed
        balance condition is satisified'''
        for i in range(N):
            for j in range(N):
                # Choose a random Cell in the Matrix
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                # Get the spin of that cell
                s = config[a, b]
                # Change the spin
                config[a, b] = config[a,b]*-1


                # Sum of the nearest neighbors
                nearest_neigh = config[(a + 1) % N, b] + config[a, (b + 1) % N] + config[(a - 1) % N, b] + config[a, (b - 1) % N]
                # change in energy
                cost = J *s* nearest_neigh
                if cost < 0:
                    s *= -1
                elif rand() < np.exp(-cost * beta):
                    s *= -1
                config[a, b] = s
        return config

    def simulate(self):
        ''' This module simulates the Ising model'''

        N, temp = 64, 5  # Initialse the lattice
        J=.2
        config = 2 * np.random.randint(2, size=(N, N)) - 1
        img_num = 0
        f = plt.figure(figsize=(10, 10), dpi=100)

        msrmnt = 1001
        for i in range(msrmnt):
            self.mcmove(config, N, 1.0 / temp, J)
            self.avg_spin.append(np.asarray(config).mean())
            avg_spin = np.asarray(config).mean()
            if i == 0:
                self.configPlot(f, config, 0, N, 1, temp, avg_spin, J)

            if i == 100:
                self.configPlot(f, config, i, N, 2, temp, avg_spin, J)
            if i == 200:
                self.configPlot(f, config, i, N, 3, temp, avg_spin, J)
            if i == 300:
                self.configPlot(f, config, i, N, 4, temp, avg_spin, J)
            if i == 400:
                self.configPlot(f, config, i, N, 5, temp, avg_spin, J)
            if i == 500:
                self.configPlot(f, config, i, N, 6, temp, avg_spin, J)
        f.show()
        plt.plot(np.linspace(0,msrmnt,msrmnt+1), self.avg_spin)
        plt.show()
    def configPlot(self, f, config, i, N, n_, temp, avg_spin, J):
        ''' This modules plts the configuration once passed to it along with time etc '''
        sp = f.add_subplot(3, 3, n_)
        avg_spin = round(avg_spin, 2)
        X, Y = np.meshgrid(range(N), range(N))
        plt.setp(sp.get_yticklabels(), visible=False)
        plt.setp(sp.get_xticklabels(), visible=False)
        plt.pcolormesh(X, Y, config, cmap=plt.cm.RdBu)
        plt.title(f't={i}, T={temp}, as={avg_spin}, J={J}')
        plt.axis('tight')




rm = Ising()
rm.simulate()

