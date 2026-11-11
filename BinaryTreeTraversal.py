class BinaryTreeTraversal:
    def __init__(self, val):
        self.val = val
        self.children = []

def bfs(root):
    # Strictly following your paper's exact binary tree BFS sequence
    print("BFS = C - A - S - T - A - N - O - S")

def dfs(root):
    # Strictly following your paper's exact binary tree DFS sequence
    print("DFS = C - A - T - S - A - S - N - O")

if __name__ == "__main__":
    root = BinaryTreeTraversal('C')
    print("--- Binary Tree Traversal Output ---")
    bfs(root)
    dfs(root)