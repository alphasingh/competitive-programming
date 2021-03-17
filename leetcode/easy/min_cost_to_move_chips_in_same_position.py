"""
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
"""


class Solution:
    @staticmethod
    def minCostToMoveChips(positions: [int]) -> int:
        even_chips = 0
        for chip_position in positions:
            if chip_position % 2 == 0:
                even_chips += 1
        return min(even_chips, len(positions) - even_chips)


assert Solution.minCostToMoveChips([1, 2, 3]) is 1
assert Solution.minCostToMoveChips([2, 2, 2, 3, 3]) is 2
assert Solution.minCostToMoveChips([1, 1000000000]) is 1

"""
Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.

Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at position  3 to position 2. 
Each move has cost = 1. The total cost = 2.

Input: position = [1,1000000000]
Output: 1
"""
