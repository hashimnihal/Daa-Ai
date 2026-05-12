# backend/algorithms/dijkstra.py

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from graphs.graph_data import graph

def dijkstra(graph, start, end):
    
    # Write Dijkstra Algorithm Here
    
    pass


if __name__ == "__main__":

    start = "A"
    end = "D"

    result = dijkstra(graph, start, end)

    print("Dijkstra Result:", result)
