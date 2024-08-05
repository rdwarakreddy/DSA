class Graph:
    def __init__(self):
        self.adjacent_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacent_list.keys():
            self.adjacent_list[vertex] = []

    def print_graph(self):
        for i in self.adjacent_list:
            print(i, ":", self.adjacent_list[i])


g = Graph()
g.addVertex("A")
g.print_graph()
