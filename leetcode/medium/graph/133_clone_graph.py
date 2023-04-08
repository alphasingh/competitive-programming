"""
https://leetcode.com/problems/clone-graph/
"""
import copy


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return copy.deepcopy(node)


graph = Node()
sol = Solution()
assert sol.cloneGraph(graph)
