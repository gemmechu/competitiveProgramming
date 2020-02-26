from typing import List


class Vertex:
    def __init__(self, val: str):
        self.val = val
        self.distance = 999
        self.neighbors = []
        self.visited = False
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, v: Vertex) -> bool:
        if v.val not in self.vertices:
            self.vertices[v.val] = v
            return True
        return False
    def add_egde(self, u: Vertex, v: Vertex):
        if u in self.vertices and v in self.vertices:
            self.vertices.get(u).add_neighbor(self.vertices.get(v))
            self.vertices.get(v).add_neighbor(self.vertices.get(u))
            return True
        return False
    def print_graph(self):
        for key in self.vertices:
            print(key," ", self.vertices[key].neighbors)
    def bfs(self, v: Vertex):
        q = list()
        q.append(v)
        v.visited = True
        while len(q)>0:
            curr = q.pop(0)

            print(curr.val)
            for vertex in curr.neighbors:
                if(not vertex.visited):
                    q.append(vertex)
                    vertex.visited = True





g= Graph()
a= Vertex('A')
b= Vertex('B')
c= Vertex('C')

g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
for i in range(ord('A'), ord('E')):
    g.add_vertex(Vertex(chr(i)))
edges = ['AB', "BC", "CA", "AD", "BE"]
for edge in edges:
    g.add_egde(edge[:1],edge[1:])
#g.print_graph()
g.bfs(a)
