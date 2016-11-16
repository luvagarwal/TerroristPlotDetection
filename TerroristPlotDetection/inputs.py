#!/usr/bin/env python

" Contains various input trees "
import networkx as nt
import matplotlib.pyplot as plt
import numpy as np

class BarabasiAlbert():
    def __init__(self, n, m, seed):
        self.n = n
        self.m = m
        self.seed = seed
        self.G = nt.barabasi_albert_graph(self.n, self.m, self.seed)
        self.R = n/5
    
    def draw_plot(self):
        nt.draw(self.G)
        plt.show()

    def GetIndividualCapabilities(self):
        capabilites = 4*np.random.rand(self.n)+1
        return capabilites

class RandomTree():
    pass

class ErdosRenyi():
    pass

def main():
	pass

if __name__ == '__main__':
	main()

