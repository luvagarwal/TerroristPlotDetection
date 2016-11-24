import numpy as numpy
import networkx as nx

#Returns a list of cut vertices of subgraph A of G
def P(A,E,V,G):
	G_A=G.subgraph(A)
	cutsets = list(nx.all_node_cuts(G_A))
	cutvertices=[]
	for i in cutsets:
		if(len(i)==1):
			cutvertices.append(i.pop())
	return cutvertices

#Return a random connected subgraph of G within hamming distance k of A
def F(v,k,A,E,V,G):
	C=list(nx.connected_component_subgraphs(G))
	np.random.shuffle(C)
	l=len(C)
	r=np.random.randint(1,l-1)
	while True:
		A_dash=set([v])
		for i in range(r):
			vert=[]
			for (u,v) in E:
				if u in A_dash and v not in A_dash:
					vert.append(v)
			A_dash.add(np.random.choice(vert))
		hammingDistance=0
		for u in V:
			if u in A and u in A_dash:
				hammingDistance+=1
		if hammingDistance<=k:
			return A_dash

def local_search(v,A,x,E,V,G):
	while True:
		for u in A:
			for w in S:
				if w not in A and (u,w) in E:
					v_star=w
					break
			break
		U_a_max=U_a(x,A.union([v_star]))
		for u in A:
			for w in S:
				if w not in A and (u,w) in E:
					if U_a_max < U_a(x,A.union([w])):
						U_a_max=U_a(x,A.union([w]))
						v_star=w
		if U_a(x,A.union([v_star]))>U_a(x,A):
			A=A.union(v_star)
		else:
			for u in A:
				if u not in P(A,E,V,G) and u is not v:
					v_star=u
					break
			U_a_max=U_a(x,A-set([v_star]))
			for u in A:
				if u not in P(A,E,V,G) and u is not v:
					if U_a_max < U_a(x,A-set([u])):
						U_a_max=U_a(x,A-set([u]))
						v_star=u
			if U_a(x,A-set([v_star])) > U_a(x,A):
				A=A-set([v_star])
			else:
				return A

def better_oa(x,y,E,V,G):
	A_better=set([])
	for v in V:
		A=local_search(v,set([v]),x,E,V,G)
		k=1
		c=0
		t=0
		while True:
			t+=1
			A_dash=F(v,k,A,E,V,G)
			A_dash=local_search(v,A_dash,x,E,V,G)
			if U_a(x,A_dash)>U_a(x,A):
				A=A_dash
				k=1
				c=0
			else:
				c+=1
				k=min(k+1,k_max)
			if c>c_max or t>t_max or U_a(x,A)>U_a(x,y):
				break
		if U_a(x,A)>U_a(x,y):
			A_better=A_better.union([frozenset(A)])
	return A_better
