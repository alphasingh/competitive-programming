"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
"""


class Solution:
    @staticmethod
    def removeStones(stones: [[int]]) -> int:
        removed = 0
        total_stones = len(stones)
        common_stones = [False] * total_stones
        visited_stones = [False] * total_stones

        def checkShared(index) -> None:
            _stone = stones[index]
            visited_stones[index] = True
            for _stone_i in range(total_stones):
                __stone = stones[_stone_i]
                share_common_row = _stone[1] == __stone[1]
                share_common_col = _stone[0] == __stone[0]
                if not visited_stones[_stone_i] and (share_common_row or share_common_col) and (_stone != __stone):
                    common_stones[_stone_i] = True
                    checkShared(_stone_i)

        for stone_i in range(total_stones):
            if not visited_stones[stone_i]:
                checkShared(stone_i)
        # print(common_stones)
        # print(visited_stones)
        for common_stone in common_stones:
            if common_stone:
                removed += 1
        return removed


assert Solution.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5
"""
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column 
with another stone still on the plane.
"""

assert Solution.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3
"""
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column 
with another stone still on the plane.
"""

assert Solution.removeStones([[0, 0]]) == 0
"""
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
"""
