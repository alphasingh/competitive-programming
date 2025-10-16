"""
https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/
"""
from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        nums.append(-1000000009)
        diffs = [0] * N
        ids = [0] * N
        start = end = 0
        for i in range(N):
            if nums[i+1] > nums[i]:
                end += 1
            else:
                diff = end - start + 1
                diffs[end] = diff
                diffs[start] = diff
                ids[start] = 0
                ids[end] = 1
                end = start = i+1
            # print(f"start={start}; end={end}; diffs={diffs}")
        # print(f"start={start}; end={end}; diffs={diffs}; ids={ids}")
        k = max(diffs)//2
        diffs.append(0)
        for i in range(N):
            if diffs[i+1] != 0 and diffs[i] != 0 and ids[i] == 1 and ids[i+1] == 0:
                diff = min(diffs[i], diffs[i+1])
                k = max(k, diff)
        # for i in range(N-3):
        #     if diffs[i] == diffs[i+1] == diffs[i+2] == diffs[i+3] == 2:
        #         k = max(k, 2)
        return max(k, 1)

sol = Solution()
assert sol.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]) == 3
assert sol.maxIncreasingSubarrays([-16,-4,14,-9,13]) == 2
assert sol.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]) == 2
assert sol.maxIncreasingSubarrays([1,2,3,4]) == 2
assert sol.maxIncreasingSubarrays([1,2,3,4,4]) == 2
assert sol.maxIncreasingSubarrays([1,1]) == 1
assert sol.maxIncreasingSubarrays([1,2,3,-10,-9,-8]) == 3
assert sol.maxIncreasingSubarrays([5,8,-2,-1]) == 2
assert sol.maxIncreasingSubarrays([-10000000,199203938]) == 1
assert sol.maxIncreasingSubarrays([9,8,-10000000,199203938,9,9]) == 1