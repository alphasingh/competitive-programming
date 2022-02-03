"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""


class Solution:
    @staticmethod
    def minReorder(n: int, connections: [[int]]) -> int:
        adj = {city: [] for city in range(n)}
        visited = [False] * n
        # print(adj, visited)
        # print(connections)
        connections = set(tuple(c) for c in connections)

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        # print(adj)
        changes = 0
        checked = set()

        to_be_visited = [0]  # start from zero
        while to_be_visited:
            popped = to_be_visited.pop()
            visited[popped] = True
            for p in adj[popped]:
                if not visited[p]:
                    to_be_visited.append(p)
                edge = (p, popped)
                if edge not in connections and edge not in checked:
                    changes += 1
                checked.add((popped, p))
                checked.add((p, popped))
            # print(to_be_visited)

        return changes


assert Solution.minReorder(n=6, connections=[[0, 1],
                                             [1, 3],
                                             [2, 3],
                                             [4, 0],
                                             [4, 5]]) == 3
"""
Explanation: Change the direction of edges show in red 
such that each node can reach the node 0 (capital).
"""
assert Solution.minReorder(n=5, connections=[[1, 0],
                                             [1, 2],
                                             [3, 2],
                                             [3, 4]]) == 2
"""
Explanation: Change the direction of edges show in red 
such that each node can reach the node 0 (capital).
"""
assert Solution.minReorder(n=3, connections=[[1, 0],
                                             [2, 0]]) == 0
