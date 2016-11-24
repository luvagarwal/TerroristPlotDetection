#!/usr/bin/env python

" Core functions "

def doTPD(Graph):
    S_dash, A_dash = lwaLP(Graph)

    while True:
        X, Y = coreLP(S_dash, A_dash)

        S_plus = betterOD(X, Y)
        S_dash.update(S_plus)

        A_plus = betterOA(x, y)
        A_dash.update(A_plus)

        if not S_plus and not A_plus:
            X, Y = coreLP(S_dash, A_dash)
            break

    return X, Y

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in xrange(1, len(s)+1))

def get_neighbours(A, Graph):
    edges = Graph.G.edges()
    neighbours = []
    for i in edges:
        if i[0] in A and i[1] in A:
            for v in A:
                if i[0] == v and i[1] != v:
                    neighbours.append(i[1])
                elif i[1] == v and i[0] != v:
                    neighbours.append(i[0])
    return list(set(neighbours))

def utility(X, S_power, A, P, G):
    def payoff(A):
        out = sum([P[v] for v in A])
        neighbours = get_neighbours(A, G)
        out += delta * sum([P[v] for v in neighbours])
        return out

    def is_overlapping(S, A):
        """
        check if defender and attacker strategies
        have overlapping vertices
        """
        return int(len(S.intersection(A)) != 0)

    tmp = [(1 - is_overlapping(S, A)) * x for S, x in zip(S_power, X)]
    tmp = sum(tmp)
    return payoff(A) * tmp

def coreLP(S_power, A_power):
    """
    Input: S_power - Defender strategy space as list
           A_power - Attacker strategy space as list
    """

    import numpy as np
    from pycpx import CPlexModel

    # Compute X assuming attacker pure strategy
    m = CPlexModel()

    U = m.new()
    X = m.new(len(S_power))

    for A in A_power:
        m.constrain(U <= -utility(X, S_power, A))

    m.constrain(sum(X) == 1)

    for x in X:
        m.constrain(x >= 0)

    m.maximize(U)
    X = m[X]

    # Compute Y assuming defender pure strategy
    m = CPlexModel()

    U = m.new()
    Y = m.new(len(A_power))

    for S in S_power:
        m.constrain(U <= utility(Y, A_power, S))

    m.constrain(sum(Y) == 1)

    for y in Y:
        m.constrain(y >= 0)

    m.maximize(U)
    Y = m[Y]

    return X, Y

def main():
    S_power = [set([1, 2, 3, 4, 5, 6, 7]), set([3]), set([4])]
    A_power = [set([2]), set([7])]
    return core_lp(S_power, A_power)

if __name__ == "__main__":
    main()