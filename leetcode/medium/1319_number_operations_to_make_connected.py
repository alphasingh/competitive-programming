"""
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""


# Python3 program for above approach

# Graph class represents a undirected graph
# using adjacency list representation
class Graph:

    def __init__(self, V):

        # No. of vertices
        self.V = V

        # Pointer to an array containing
        # adjacency lists
        self.adj = [[] for i in range(self.V)]

    # Function to return the number of
    # connected components in an undirected graph
    def NumberOfconnectedComponents(self):

        # Mark all the vertices as not visited
        visited = [False for i in range(self.V)]

        # To store the number of connected
        # components
        count = 0

        for v in range(self.V):
            if (visited[v] == False):
                self.DFSUtil(v, visited)
                count += 1

        return count

    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.adj[v]:
            if (not visited[i]):
                self.DFSUtil(i, visited)

    # Add an undirected edge
    def addEdge(self, v, w):

        self.adj[v].append(w)
        self.adj[w].append(v)


# Driver code
# if __name__=='__main__':

# 	g = Graph(5)
# 	g.addEdge(1, 0)
# 	g.addEdge(2, 3)
# 	g.addEdge(3, 4)

# 	print(g.NumberOfconnectedComponents())

# This code is contributed by rutvik_56


class Solution:
    def makeConnected(self, n: int, connections: [[int]]) -> int:
        graph = Graph(n)
        for connection in connections:
            graph.addEdge(connection[0], connection[1])
        number_of_components = graph.NumberOfconnectedComponents()
        required = -1
        number_of_edges = len(connections)
        if number_of_edges >= n - 1:
            required = number_of_components - 1
        return required


sol = Solution()
assert sol.makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]) == 1
# Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

assert sol.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2

assert sol.makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]) == -1
# Explanation: There are not enough cables.

assert sol.makeConnected(n=5, connections=[[0, 1], [0, 2], [3, 4], [2, 3]]) == 0
# Explanation: Already connected
