import numpy as np

def  better_od(x, y, V, R):
    S_better = set()
    for v in V:
        #Starting from v, form S by adding all those vertices which increases the utility in a greedy approach
        S = set([v])
        while len(S) < R:
        	U_d_max = 0
            for v_i in V:
            	tmp = U_d(S.union([v_i]), y)
                if tmp > U_d_max:
                    v_star = v_i
                    U_d_max = tmp
            S = S.union([v_star])
        #If S gives better result than x, include its vertices as part of the solution
        if U_d(S,y) > U_d(x,y):
            S_better = S_better.union([frozenset(S)])
    return S_better
