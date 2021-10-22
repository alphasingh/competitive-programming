class Solution:
    @staticmethod
    def orangesRotting(grid: [[int]]) -> int:
        minutes = 0
        m = len(grid)
        n = len(grid[0])

        def anyRottenNeighbor(r, c) -> bool:
            up = r > 0 and grid[r - 1][c] == 2
            down = r < m - 1 and grid[r + 1][c] == 2
            right = c > 0 and grid[r][c - 1] == 2
            left = c < n - 1 and grid[r][c + 1] == 2
            return up or down or right or left

        while True:
            rot_next = []
            for i in range(m):
                for j in range(n):
                    # fresh orange has any rotten neighbor
                    if grid[i][j] == 1 and anyRottenNeighbor(i, j):
                        rot_next.append((i, j))
            # print(rot_next)
            if not rot_next:
                break
            # rot the neighbors of rotten oranges
            for to_be_rotten in rot_next:
                i, j = to_be_rotten[0], to_be_rotten[1]
                grid[i][j] = 2
            minutes += 1

        # count all fresh oranges
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
        return minutes if fresh == 0 else -1


assert Solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
assert Solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
"""
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.
"""
assert Solution.orangesRotting([[0, 2]]) == 0
"""
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
