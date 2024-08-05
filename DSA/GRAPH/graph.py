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
            if v2 not in self.adjacent_list[v1]:
                self.adjacent_list[v1].append(v2)
            if v1 not in self.adjacent_list[v2]:
                self.adjacent_list[v2].append(v1)
        else:
            print(f"One or both vertices {v1} and {v2} do not exist.")

    def removeEdge(self, v1, v2):
        if v1 in self.adjacent_list and v2 in self.adjacent_list:
            self.adjacent_list[v1].remove(v2)
            self.adjacent_list[v2].remove(v1)


# Test Edge Cases
g = Graph()

# Edge case 1: Adding an edge between non-existent vertices
g.addEdge("X", "Y")  # Should handle gracefully

# Edge case 2: Adding duplicate edges
g.addVertex("A")
g.addVertex("B")
g.addEdge("A", "B")
g.addEdge("A", "B")  # Should not create a duplicate edge

# Edge case 3: Adding a self-loop
g.addEdge("A", "A")  # Should handle self-loop

# Edge case 4: Printing an empty graph
empty_graph = Graph()
empty_graph.print_graph()  # Should print nothing

# Edge case 5: Adding vertices with the same name
g.addVertex("A")  # Should inform that vertex "A" already exists

# Standard case
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")

g.addEdge("A", "C")
g.addEdge("A", "D")
g.addEdge("B", "D")

# Print the graph to verify the edges
g.print_graph()
