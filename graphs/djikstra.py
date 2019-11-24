

class Vertex(object):

    def __init__(self, id):
        self.id = id
        self.adj = []


class Edge(object):

    def __init__(self, v1, v2, w):
        self.v1 = v1
        self.v2 = v2
        self.w = w


class Graph(object):

    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.append(v)

    def add_edge(self, v1, v2, w):

        self.edges.append(Edge(v1, v2, w))

        self.add_vertex(v1)
        self.add_vertex(v2)

        v1.adj.append((v2, w))
        v2.adj.append((v1, w))


class PriorityQueue(object):

    def __init__(self):
        self.el = []
        self.el_pos = {}

    def update(self, ):
        pass

    def insert(self):
        pass

    def extract_min(self):
        pass


def djikstra_shortest_path(g, s):

    dist = {}
    visited = set()
    q = PriorityQueue()

    dist[s.id] = 0
    q.insert((s, 0))

    while q:

        curr = q.extract_min()
        visited.add(curr)
        curr_d = dist.get(curr)

        for e in curr.adj:
            v, w = e
            if v in visited:
                continue

            d = dist.get(v.id)

            if not d or curr_d + w < d:
                dist[v.id] = curr_d + w
                q.update((v.id, curr_d + w))


def main():

    a = Vertex(1)
    b = Vertex(2)
    c = Vertex(3)
    d = Vertex(4)

    G = Graph()

    G.add_edge(a, b, 1)
    G.add_edge(a, c, 4)
    G.add_edge(b, c, 2)
    G.add_edge(b, d, 4)
    G.add_edge(c, d, 1)


if __name__ == "__main__":
    main()
