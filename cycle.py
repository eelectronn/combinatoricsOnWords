import itertools as it
import networkx as nx


def create_de_bruijn_graph(k, n):
    G = nx.MultiDiGraph()
    alphabet = [str(_) for _ in range(k)]
    nodes = [''.join(tup) for tup in list(it.product(alphabet, repeat=n))]
    G.add_nodes_from(nodes)
    for node in nodes:
        for letter in alphabet:
            G.add_edge(node, node[1:]+letter, weight=node+letter)
    return G


def print_l_cycle(G, l):
    cyc = nx.algorithms.simple_cycles(G)
    for c in cyc:
        if len(c) <= l:
            yield c


test = [(2, 3), (2, 5), (3, 3), (2, 7), (3, 5)]
f = open('results.txt', 'aw', 1)
f.write('results start\n')
for t in test:
    print('k:', t[0], 'n:', t[1])
    f.write('k: ' + str(t[0]) + ' n: ' + str(t[1]) + '\n')
    G = create_de_bruijn_graph(t[0], t[1])
    cyc = print_l_cycle(G, t[1])
    for c in cyc:
        print(c)
        f.write(str(c) + '\n')
    f.write('-------------------\n')
    print('-------------------')

