# backend/algorithms/astar.py

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from graphs.graph_data import graph

def astar(graph, start, end):

    # Write A* Algorithm Here

    pass


if __name__ == "__main__":

    start = "A"
    end = "D"

    result = astar(graph, start, end)

    print("A* Result:", result)
