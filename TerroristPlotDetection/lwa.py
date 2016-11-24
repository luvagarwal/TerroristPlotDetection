import random

from inputs import BarabasiAlbert
from pycpx import CPlexModel
import numpy as np

def lwaLp(graph_object):
	capabilites = graph_object.capabilities
	no_vertices = graph_object.n
	m = CPlexModel()
	cv = m.new(no_vertices, vtype = float, ub = 1, lb =0)
	U = m.new(vtype = float)
	diag = np.diag(capabilites)
	m.constrain(U <= -diag*(1-cv))
	m.constrain(sum(cv) <= graph_object.R)
	m.maximize(U)
	start = findStrategySet(m[cv], graph_object.R)
	return start

def findStrategySet(cv, R):
    prefix = [cv[0]]
    for c in cv[1:]:
        prefix.append(prefix[-1] + c)

    y = random.random()
    start = 0
    ans = []
    for i in xrange(R):
        y = y + i
        while start < len(prefix) and prefix[start] <= y:
            start += 1
        ans.append(start)
    print ans
    return ans

def main():
	g1 = np.array([BarabasiAlbert(20,1,1), BarabasiAlbert(40,1,1), BarabasiAlbert(60,1,1), BarabasiAlbert(80,1,1), BarabasiAlbert(100,1,1)])
	

	lwaLp(g1[0])
	#g1.draw_plot()

if __name__ == '__main__':
	main()