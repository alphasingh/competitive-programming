"""
https://leetcode.com/problems/game-of-life/
"""


class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        print(board)


sol = Solution()
assert sol.gameOfLife(board=[[0, 1, 0],
                             [0, 0, 1],
                             [1, 1, 1],
                             [0, 0, 0]]) == [[0, 0, 0],
                                             [1, 0, 1],
                                             [0, 1, 1],
                                             [0, 1, 0]]
assert sol.gameOfLife(board=[[1, 1],
                             [1, 0]]) == [[1, 1],
                                          [1, 1]]
