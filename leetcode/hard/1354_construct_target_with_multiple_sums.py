"""
https://leetcode.com/problems/construct-target-array-with-multiple-sums/
"""

import heapq


class Solution:
    def isPossible(self, target: [int]) -> bool:
        ideal = len(target)
        for i in range(ideal):
            target[i] = -target[i]  # negate the elements to pop maximum from heap
        heapq.heapify(target)  # heapify
        current_sum = sum(target)
        ideal = -ideal
        # print(target, current_sum)
        while current_sum < ideal:  # reduce sum
            current_max = heapq.heappop(target)
            others = current_sum - current_max
            if current_max > others:
                break
            to_be_pushed = current_max - others
            current_sum -= others
            heapq.heappush(target, to_be_pushed)
            # print(target, 'sum', current_sum, 'max', current_max)
        return current_sum == ideal and set(target) == {-1}


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
