import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from graphs.graph_data import graph

def dijkstra(graph, start, end):
    dist = {}
    visited = {}
    parent = {}
    for vertex in graph:
        dist[vertex] = 999
        visited[vertex] = 0
        parent[vertex] = None
    dist[start]=0
    parent[start] = start

    for i in range(len(graph)):
        min_vertex = find_min(dist, visited, graph)
        visited[min_vertex]=1

        for vertex, distance in graph[min_vertex].items():
            if(dist[vertex]>dist[min_vertex]+distance and visited[vertex]==0):
                dist[vertex]=dist[min_vertex]+distance
                parent[vertex] = min_vertex
    path = route(parent,end)
    return dist[end], path

def find_min(dist, visited, graph):
    min_value = 999
    for vertex in graph:
        if(dist[vertex]<min_value and visited[vertex]==0):
            min_value = dist[vertex]
            min_vertex = vertex
    return min_vertex

def route(parent, end):
    node=end
    path = []
    while(parent[node] != node):
           path.append(node)
           node=parent[node]
    path.append(node)
    path.reverse()
    return path

if __name__ == "__main__":
    start = "A"
    end = "D"
    parent = {}
    result, path  = dijkstra(graph, start, end)
    print("Dijkstra Result:", result)
    print("Dijkstra Path:", path)