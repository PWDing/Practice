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

    def set_color(self, color):
        self.color = color

    def set_distance(self, distance):
        self.distance = distance

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def add_neighbor(self, neighbor, weight=0):
        self.connected_nodes[neighbor] = weight

    def get_connections(self):
        return self.connected_nodes.keys()

    def get_id(self):
        return self.id

    def get_color(self):
        return self.color

    def get_distance(self):
        return self.distance

    def get_weight(self, neighbor):
        return self.connected_nodes[add_neighbor]


# word ladder problem
def build_word_graph(word_file):
    word_dict = {}
    word_graph = Graph()
    # create buckets of words that differ by one letter
    with open(word_file) as wf:
        for line in wf:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in word_dict:
                    word_dict[bucket].append(word)
                else:
                    word_dict[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in word_dict.keys():
        for word1 in word_dict[bucket]:
            for word2 in word_dict[bucket]:
                if word1 != word2:
                    word_graph.add_edge(word1, word2)
    return word_graph


def bfs(agraph, start):
    start.set_distance(0)
    start.set_predecessor(None)
    vertex_queue = Queue()
    vertex_queue.enqueue(start)
    while vertex_queue.size() > 0:
        current = vertex_queue.dequeue()
        for neighbor in current.get_connections():
            if neighbor.get_color() == 'white':
                neighbor.set_color('gray')
                neighbor.set_distance(current.get_distance()+1)
                neighbor.set_predecessor(current)
                vertex_queue.enqueue(neighbor)
        current.set_color('black')


def traverse(node):
    path = node
    while path.get_predecessor():
        print(path.get_id)
        path = path.get_predecessor()
    print(path.get_id())


# The Knight's Tour puzzle, cheeseboard means board size
def build_knight_graph(cheeseboard):
    knight = Graph()
    for row in range(cheeseboard):
        for col in range(cheeseboard):
            node = position_to_node(row, col, cheeseboard)
            next_positions = get_legal_moves(row, col, cheeseboard)
            for pos in next_positions:
                next_node = position_to_node(pos[0], pos[1], cheeseboard)
                knight.add_edge(node, next_node)
    return knight


def position_to_node(row, col, cheeseboard):
    return row * cheeseboard + col


def get_legal_moves(pos_x, pos_y, cheeseboard):
    next_moves = []
    move_offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for offset in move_offsets:
        next_x = pos_x + offset[0]
        next_y = pos_y + offset[1]
        if check_coord(next_x) and check_coord(next_y):
            next_moves.append((next_x, next_y))
    return next_moves


def check_coord(x, cheeseboard):
    if x >= 0 and x < cheeseboard:
        return True
    else:
        return False


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
