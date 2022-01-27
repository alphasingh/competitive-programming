"""
https://leetcode.com/problems/find-the-most-competitive-subsequence/
"""

import heapq


class Solution:
    @staticmethod
    def mostCompetitive(nums: [int], k: int) -> [int]:
        # heap
        n = len(nums)
        c = nums[n - k:]
        # print(c)
        heap = []  # (nums[i], i)
        heapq.heapify(heap)
        j = -k
        for i in range(n - k):
            heapq.heappush(heap, (nums[i], i))
        # print(heap)
        used = 0
        while heap and j < 0:
            heapq.heappush(heap, (nums[j], n + j))
            # print('heap', heap)
            smallest, index = heapq.heappop(heap)
            # print('smallest', smallest, index)
            while heap and index < used:
                smallest, index = heapq.heappop(heap)
            # print(smallest, index)
            # print('heap after popping', heap)
            used = index
            c[j] = smallest
            j += 1
            # print(c, used)
        return c


assert Solution.mostCompetitive(nums=[3, 5, 2, 6], k=2) == [2, 6]
"""
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, 
[2,6] is the most competitive.
"""
assert Solution.mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4) == [2, 3, 3, 4]
