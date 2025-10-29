"""
https://leetcode.com/problems/make-array-elements-equal-to-zero/
3354. Make Array Elements Equal to Zero
"""
from typing import List


class Solution:

    def __init__(self):
        self.total = 0

    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        backup = nums.copy()
        self.total = 0

        def do(arr, curr, direction):
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += direction
                    continue
                arr[curr] -= 1
                direction = -direction
                curr += direction
            self.total += int(set(arr) == {0})

        for i in range(n):
            # print(f"i{i};backup:{backup};nums:{backup.copy()};total:{self.total}")
            if backup[i] == 0:
                do(backup.copy(), i, +1)
                do(backup.copy(), i, -1)
        return self.total


sol = Solution()
assert sol.countValidSelections([1,0,2,0,3]) == 2
assert sol.countValidSelections([2,3,4,0,4,1,0]) == 0
long_test = ([35,30,33,32,29,31,33,27,30,38,36,31,29,29,32,35,28] + [0]*68 +
              [35,43,33,36,32,34,37,31,41,34,30,37,35,43,36])
assert sol.countValidSelections(long_test) == 68