"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""


class Solution:
    @staticmethod
    def search(nums: [int], target: int) -> bool:

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return True
            while l < m and nums[l] == nums[m]:
                l += 1

            # sorted first half
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False


assert Solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0) is True
assert Solution.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3) is False
