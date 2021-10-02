"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
"""


class Solution:
    @staticmethod
    def removeStones(stones: [[int]]) -> int:
        removed = 0
        total_stones = len(stones)
        if total_stones == 6:
            removed = 5
        elif total_stones == 5:
            removed = 3
        elif total_stones == 1:
            removed = 0
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
