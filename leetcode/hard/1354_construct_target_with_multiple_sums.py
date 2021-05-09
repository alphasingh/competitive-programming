"""
https://leetcode.com/problems/construct-target-array-with-multiple-sums/
"""

import heapq


class Solution:
    def isPossible(self, target: [int]) -> bool:
        total = sum(target)
        target = [-a for a in target]
        heapq.heapify(target)
        while True:
            a = -heapq.heappop(target)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(target, -a)


sol = Solution()
assert sol.isPossible([1, 1000000000]) is True
assert sol.isPossible([9, 9, 9]) is False
assert sol.isPossible([9, 3, 5]) is True
"""
Explanation: Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
"""
assert sol.isPossible([1, 1, 1, 2]) is False
"""
Explanation: Impossible to create target array from [1,1,1,1].
"""
assert sol.isPossible([8, 5]) is True
