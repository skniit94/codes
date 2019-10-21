class Vertex(object):

    def __init__(self, data):
        self.data = data
        self.adj = []


def dfs(root):
    visited = set()
    st = list()
    st.append(root)
    while st:
        curr = st.pop()
        if curr in visited:
            continue
        visited.add(curr)
        print (curr.data, end = ' ')
        for adj in curr.adj:
            st.append(adj)
    print()


def bfs(root):
    visited = set()
    q = list()
    q.append(root)
    while q:
        curr = q.pop(0)
        if curr in visited:
            continue
        visited.add(curr)
        print (curr.data, end = ' ')
        for adj in curr.adj:
            q.append(adj)
    print()


def main():
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    v6 = Vertex(6)

    v1.adj = [v2]
    v2.adj = [v3, v4]
    v3.adj = [v4, v6]
    v4.adj = [v5]
    v5.adj = [v2]
    v6.adj = [v4]

    bfs(v1)
    dfs(v1)


if __name__ == '__main__':
    main()
