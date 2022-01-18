"""
https://leetcode.com/problems/remove-stones-to-minimize-the-total/
"""

import heapq
from math import floor


class Solution:
    @staticmethod
    def minStoneSum(piles: [int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        # print(heap)
        while k:
            # exit if all stones = 1
            if heap[0] == -1:
                break
            stones = heapq.heappop(heap)
            # remove half stones
            stones += floor(-stones / 2)
            if stones < 0:
                heapq.heappush(heap, stones)
            k -= 1
            # print(heap)
        # print(k)
        return -sum(heap)


assert Solution.minStoneSum(piles=[5, 4, 9], k=2) == 12
"""
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.
"""
assert Solution.minStoneSum(piles=[4, 3, 6, 7], k=3) == 12
"""
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,3,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones in [2,3,3,4] is 12.
"""
