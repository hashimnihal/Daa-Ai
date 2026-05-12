# backend/algorithms/greedy.py

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from graphs.graph_data import graph

def greedy(graph, start, end):

    # Write Greedy Algorithm Here

    pass


if __name__ == "__main__":

    start = "A"
    end = "D"

    result = greedy(graph, start, end)

    print("Greedy Result:", result)
