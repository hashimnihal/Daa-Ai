# backend/visualization/matplotlib_visual.py
import os
import sys
import matplotlib.pyplot as plt
import networkx as nx

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from graphs.graph_data import graph


def plot_graph():

    # Create directed graph
    G = nx.DiGraph()

    # Add edges and weights
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    # Set graph layout
    pos = nx.spring_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=2500)

    # Draw edges
    nx.draw_networkx_edges(
        G,
        pos,
        arrowstyle='->',
        arrowsize=20,
        width=2
    )

    # Draw node labels
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=14,
        font_weight='bold'
    )

    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=12
    )

    # Title
    plt.title("Greedy Algorithm Graph Visualization")

    # Remove axis
    plt.axis('off')

    # Show graph
    plt.show()


if __name__ == "__main__":

    plot_graph()
