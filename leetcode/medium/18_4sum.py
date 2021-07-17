"""
https://leetcode.com/problems/4sum-ii/
"""

import bisect


class Solution:

    @staticmethod
    def fourSum(nums: [int], target: int) -> [[int]]:
        nums.sort()
        n, count = len(nums), 0
        combinations = []
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    abc = nums[a] + nums[b] + nums[c]
                    rem = target - abc
                    index_l = bisect.bisect_left(nums, rem)
                    index_r = bisect.bisect_right(nums, rem)
                    # print(index_l, index_r)
                    if n > index_l != index_r and index_r > c and index_l != a and index_l != b and index_l != c and \
                            nums[index_l] == rem:
                        combinations.append(tuple(sorted((nums[a], nums[b], nums[c], rem))))
                        count += 1
        # print(count)
        # print(set(combinations))
        combinations = list(list(combo) for combo in set(combinations))
        # print(combinations)
        return combinations


assert sorted(Solution.fourSum(nums=[2, 2, 2, 2, 2], target=8)) == [[2, 2, 2, 2]]
assert sorted(Solution.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
assert sorted(Solution.fourSum([-5, 5, 4, -3, 0, 0, 4, -2], 4)) == [[-5, 0, 4, 5], [-3, -2, 4, 5]]
