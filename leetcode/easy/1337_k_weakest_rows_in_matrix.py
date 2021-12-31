"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""

import heapq


class Solution:
    @staticmethod
    def kWeakestRows(mat: [[int]], k: int) -> [int]:
        max_heap = []
        for i in range(len(mat)):
            heapq.heappush(max_heap, [mat[i].count(1), i])
        return [heapq.heappop(max_heap)[1] for _ in range(k)]


assert Solution.kWeakestRows(mat=
                             [[1, 1, 0, 0, 0],
                              [1, 1, 1, 1, 0],
                              [1, 0, 0, 0, 0],
                              [1, 1, 0, 0, 0],
                              [1, 1, 1, 1, 1]],
                             k=3) == [2, 0, 3]
"""
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
"""
assert Solution.kWeakestRows(mat=
                             [[1, 0, 0, 0],
                              [1, 1, 1, 1],
                              [1, 0, 0, 0],
                              [1, 0, 0, 0]],
                             k=2) == [0, 2]
"""
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
"""
