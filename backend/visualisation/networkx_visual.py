# backend/visualization/networkx_visual.py

import os
import sys
import networkx as nx
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from graphs.graph_data import graph


def visualize_graph():

    # Create graph
    G = nx.Graph()

    # Add edges from graph dictionary
    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    # Position layout
    pos = nx.spring_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color="skyblue",
        node_size=800
    )

    # Draw edges
    nx.draw_networkx_edges(
        G,
        pos,
        width=2
    )

    # Draw labels
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=10,
        font_weight="bold"
    )

    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels
    )

    plt.title("Graph Visualization")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":

    visualize_graph()
