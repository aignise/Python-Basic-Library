class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph.keys():
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices."""
        if vertex1 in self.graph.keys():
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

    def show_edges(self):
        """Display the edges of the graph."""
        return [(k, v) for k, v_list in self.graph.items() for v in v_list]
