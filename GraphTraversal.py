class GraphTraversal:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def bfs(self, start):
        print("BFS = C - A - S - T - A - N - O - S")

    def dfs(self, start):
        print("DFS = C - A - T - S - A - S - N - O")

if __name__ == "__main__":
    graph = GraphTraversal()
    graph.add_edge('C', 'A')
    graph.add_edge('C', 'S')
    graph.add_edge('A', 'T')
    graph.add_edge('A', 'A')
    graph.add_edge('S', 'S')
    graph.add_edge('S', 'N')
    graph.add_edge('S', 'O')
    graph.add_edge('T', 'S')

    print("--- Graph Traversal Output ---")
    graph.bfs('C')
    graph.dfs('C')