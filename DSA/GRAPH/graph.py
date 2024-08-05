class Graph:
    def __init__(self):
        self.adjacent_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacent_list:
            self.adjacent_list[vertex] = []
        else:
            print(f"Vertex {vertex} already exists.")

    def print_graph(self):
        for vertex in self.adjacent_list:
            print(vertex, ":", self.adjacent_list[vertex])

    def addEdge(self, v1, v2):
        if v1 in self.adjacent_list and v2 in self.adjacent_list:
            self.adjacent_list[v1].append(v2)
            self.adjacent_list[v2].append(v1)
        else:
            print(f"One or both vertices {v1} and {v2} do not exist.")

    def removeEdge(self, v1, v2):
        if v1 in self.adjacent_list and v2 in self.adjacent_list:
            self.adjacent_list[v1].remove(v2)
            self.adjacent_list[v2].remove(v1)

    def print_edges(self):
        edges = []
        for key, values in self.adjacent_list.items():
            for value in values:
                if (key, value) not in edges and (value, key) not in edges:
                    edges.append((key, value))
        return edges

    def removeVertex(self, vertex):
        for i in self.adjacent_list[vertex]:
            self.adjacent_list[i].remove(vertex)
        del self.adjacent_list[vertex]

    def BFS(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for i in self.adjacent_list[current_vertex]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)


# Test Edge Cases
g = Graph()

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "C")
g.addEdge("C", "D")
g.addEdge("D", "E")
g.print_graph()
g.BFS("A")
