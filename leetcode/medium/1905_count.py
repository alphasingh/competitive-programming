"""
https://leetcode.com/problems/count-sub-islands/
"""


class Solution:
    @staticmethod
    def countSubIslands(grid1: [[int]], grid2: [[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        seen = [[False] * n for row in range(m)]
        islands = {}
        sub_islands = 0

        # keep visiting neighbors until you cannot
        def bfs(r, c, island_id):
            inbound = (0 <= r < m) and (0 <= c < n)
            if not inbound or not grid2[r][c] or seen[r][c]:
                return

            seen[r][c] = True
            islands[island_id].append((r, c))

            # check adjacent cells
            bfs(r - 1, c, island_id)
            bfs(r + 1, c, island_id)
            bfs(r, c - 1, island_id)
            bfs(r, c + 1, island_id)

        # find all the islands in grid2
        for i in range(m):
            for j in range(n):
                if grid2[i][j] and not seen[i][j]:
                    islands[sub_islands] = []
                    bfs(i, j, sub_islands)
                    sub_islands += 1

        # all islands in grid2
        # print(islands, sub_islands)
        for island in islands.values():
            # all cells should exist in grid1 too
            for r, c in island:
                if not grid1[r][c]:
                    sub_islands -= 1
                    break

        return sub_islands


assert Solution.countSubIslands(
    grid1=[[1, 1, 1, 0, 0],
           [0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 1, 1]],
    grid2=[[1, 1, 1, 0, 0],
           [0, 0, 1, 1, 1],
           [0, 1, 0, 0, 0],
           [1, 0, 1, 1, 0],
           [0, 1, 0, 1, 0]]) == 3

assert Solution.countSubIslands(
    grid1=[[1, 0, 1, 0, 1],
           [1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1],
           [1, 0, 1, 0, 1]],
    grid2=[[0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1],
           [0, 1, 0, 1, 0],
           [0, 1, 0, 1, 0],
           [1, 0, 0, 0, 1]]) == 2
