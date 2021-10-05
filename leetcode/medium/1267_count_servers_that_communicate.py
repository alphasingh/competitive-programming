"""
https://leetcode.com/problems/count-servers-that-communicate/
"""


class Solution:
    @staticmethod
    def countServers(grid: [[int]]) -> int:
        row = {}
        col = {}
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:  # server
                    if i not in row:
                        row[i] = 0
                    if j not in col:
                        col[j] = 0
                    row[i] += 1
                    col[j] += 1
        # print(row)
        # print(col)
        connected = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (row[i] > 1 or col[j] > 1):
                    connected += 1
        return connected


assert Solution.countServers([[1, 0], [0, 1]]) == 0
# Explanation: No servers can communicate with others.
assert Solution.countServers([[1, 0], [1, 1]]) == 3
# Explanation: All three servers can communicate with at least one other server.
assert Solution.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == 4
"""
Explanation: The two servers in the first row can communicate with each other. 
The two servers in the third column can communicate with each other. 
The server at right bottom corner can't communicate with any other server.
"""
