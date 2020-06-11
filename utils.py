"""
Created on June 04, 2020

@author: Harsh N. Patel

"""

import networkx as nx
from pyvis.network import Network


def get_l_cycle(G, l):
    cyc = nx.algorithms.simple_cycles(G)
    for c in cyc:
        if len(c) <= l:
            yield c


def plot_graph(G):
    options = {
        'height': '800px',
        'width': '100%',
        'bgcolor': '#222222',
        'font_color': 'black'
    }
    net = Network(notebook=True, **options, directed=True)
    for node in G.nodes:
        net.add_node(node, color='white', shape='circle')
    for edge in G.edges:
        net.add_edge(edge[0], edge[1], color='green')
    net.toggle_physics(False)
    # net.show_buttons(filter_=['edges'])
    return net.show('example.html')
