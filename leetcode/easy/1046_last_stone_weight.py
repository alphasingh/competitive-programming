"""
https://leetcode.com/problems/merge-sorted-array/
"""
import heapq


class Solution:
    @staticmethod
    def lastStoneWeight(stones: [int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        # print(max_heap)
        size = len(max_heap)
        if size == 1:
            return -max_heap[0]
        while size >= 2:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            size -= 2
            if first > second:
                heapq.heappush(max_heap, -(first - second))
                size += 1
        return -heapq.heappop(max_heap) if max_heap else 0


assert Solution.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]) == 1
"""
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
"""
assert Solution.lastStoneWeight(stones=[1]) == 1
assert Solution.lastStoneWeight(stones=[1, 1]) == 0
"""
Explanation: 
We combine 1 and 1 to get nothing as they are equal.
We will be left with nothing after smashing equal stones.
"""
