# assign3p2.py

class Graph:
    def __init__(self):
        """
        Initialize an empty graph using adjacency list representation.
        """
        self.graph = {}   # dictionary: node → list of neighbors

    def add_edge(self, u, v):
        """
        Add an undirected edge between nodes u and v.
        If a node does not exist, create its adjacency list.
        """
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        # Add each node to the other's adjacency list
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        """
        Perform recursive Depth-First Search starting from node 'start'.
        Return the list of nodes in the DFS traversal order.
        """
        visited = set()
        result = []

        def dfs_recursive(node):
            visited.add(node)
            result.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result


# ----------------- TESTING CODE -----------------
if __name__ == "__main__":

    # Test Case 1: Simple linear graph
    g1 = Graph()
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    print(f"DFS from 0: {g1.dfs(0)}")  # Expected: [0, 1, 2, 3]

    # Test Case 2: Tree structure
    g2 = Graph()
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 3)
    g2.add_edge(1, 4)
    g2.add_edge(2, 5)
    print(f"DFS from 0: {g2.dfs(0)}")  # One possible: [0, 1, 3, 4, 2, 5]

    # Test Case 3: Graph with cycle
    g3 = Graph()
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 0)  # Creates cycle
    g3.add_edge(2, 3)
    print(f"DFS from 0: {g3.dfs(0)}")  # Expected: [0, 1, 2, 3]
