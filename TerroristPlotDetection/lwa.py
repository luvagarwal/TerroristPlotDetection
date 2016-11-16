from inputs import BarabasiAlbert
from pycpx import CPlexModel
import numpy as np

def LwaLp(graph_object):
	capabilites = graph_object.GetIndividualCapabilities()
	no_vertices = graph_object.n
	m = CPlexModel()
	cv = m.new(no_vertices, vtype = float, ub = 1, lb =0)
	U = m.new(vtype = float)
	diag = np.diag(capabilites)
	m.constrain(U <= -diag*(1-cv))
	m.constrain(sum(cv) <= graph_object.R)
	m.maximize(U)
	print(m[cv])


def main():
	g1 = BarabasiAlbert(20,1,1)
	LwaLp(g1)
	#g1.draw_plot()

if __name__ == '__main__':
	main()