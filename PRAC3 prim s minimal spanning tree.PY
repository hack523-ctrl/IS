

import heapq
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list) 
    def add_edge(self, u, v, weight):
        """Add an undirected edge with a weight"""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    def prim_mst(self):
        mst = []
        visited = [False] * self.V
        min_heap = [(0, 0, -1)]  
        while min_heap and len(mst) < self.V - 1:
            weight, u, parent = heapq.heappop(min_heap)
            if not visited[u]:
                visited[u] = True
                if parent != -1:
                    mst.append((parent, u, weight))
                for v, w in self.graph[u]:
                    if not visited[v]:
                        heapq.heappush(min_heap, (w, v, u))
        return mst
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)
    mst = g.prim_mst()
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")


