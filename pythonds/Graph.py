from pythonds.Queue import Queue


class Graph:
    def __init__(self):
        self.vertices = {} 
        self.vertex_num = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, node):
        return node in self.vertices

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        self.vertex_num += 1
        return self.vertices

    def get_vertex(self, node):
        if node in self.vertices:
            return self.vertices[node]

    def get_vertices(self):
        return self.vertices.keys()

    def add_edge(self, begin, end, weight):
        if begin not in self.vertices:
            self.add_vertex(begin)
        if end not in self.vertices:
            self.add_vertex(end)
        self.vertices[begin].add_neighbor(self.vertices[end], weight)


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_nodes = {}
        self.color = 'white'
        self.distance = 0
        self.predecessor = None

    def __str__(self):
        return str(self.id) + ' Connected to: '\
               + str([x.id for x in self.connected_nodes])

    def add_neighbor(self, neighbor, weight=0):
        self.connected_nodes[neighbor] = weight

    def get_connections(self):
        return self.connected_nodes.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_nodes[add_neighbor]


if __name__ == '__main__':
    my_graph = Graph()
    for i in range(10):
        my_graph.add_vertex(i)
    my_graph.add_edge(0, 1, 5)
    my_graph.add_edge(0, 5, 2)
    my_graph.add_edge(1, 2, 4)
    my_graph.add_edge(2, 3, 9)
    my_graph.add_edge(3, 4, 7)
    my_graph.add_edge(3, 5, 3)
    my_graph.add_edge(4, 0, 1)
    my_graph.add_edge(5, 4, 8)
    my_graph.add_edge(5, 2, 1)

    for vertex in my_graph:
        for neighbor in vertex.get_connections():
            print("(%s, %s)" % (vertex.get_id(), neighbor.get_id()))
