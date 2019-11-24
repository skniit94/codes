class Vertex(object):

    def __init__(self, id):
        self.id = id
        self.adj = []  # will contain tuples (Vertex, Weight)


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


def dfs(g):

    visited = set()
    st = []

    for v in g.vertices:

        if v in visited:
            continue
        st.append(v)
        visited.add(v)
        while st:
            curr = st.pop()
            print (curr.id)
            for tup in curr.adj:
                adj = tup[0]
                if adj in visited:
                    continue
                st.append(adj)
                visited.add(adj)


def bfs(g):

    visited = set()
    q = []

    for v in g.vertices:

        if v in visited:
            continue
        q.append(v)
        visited.add(v)
        while q:
            curr = q.pop(0)
            print (curr.id)
            for tup in curr.adj:
                adj = tup[0]
                if adj in visited:
                    continue
                q.append(adj)
                visited.add(adj)


def main():

    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    h = Vertex('h')
    i = Vertex('i')

    Gr = Graph()

    Gr.add_edge(a, b, 2)
    Gr.add_edge(b, c, 3)
    Gr.add_edge(b, d, 1)
    Gr.add_edge(c, d, 7)
    Gr.add_edge(d, e, 4)
    Gr.add_edge(e, f, 6)
    Gr.add_edge(f, g, 9)
    Gr.add_edge(f, h, 5)

    Gr.add_vertex(i)

    dfs(Gr)
    bfs(Gr)




if __name__ == "__main__":
    main()