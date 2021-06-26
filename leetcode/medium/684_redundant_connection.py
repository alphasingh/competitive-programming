"""
https://leetcode.com/problems/redundant-connection/
"""


class Solution:
    def findRedundantConnection(self, edges: [[int]]) -> [int]:
        self.__str__()
        redundant_edge = edges[-1]
        return redundant_edge


sol = Solution()
assert sol.findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]]) == [2, 3]
assert sol.findRedundantConnection(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
