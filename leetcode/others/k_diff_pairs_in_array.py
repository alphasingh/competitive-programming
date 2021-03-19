"""
532. K-diff Pairs in an Array
https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""


class Solution:
    @staticmethod
    def find_pairs(nums: [int], k: int) -> int:
        valid_pair_count = 0
        valid_pairs = set()
        n = len(nums)
        if k == 0:
            for num in set(nums):
                if nums.count(num) >= 2:
                    valid_pairs.add(num)
                    valid_pair_count += 1
        else:
            for i in range(n):
                for j in range(i + 1, n):
                    if nums[i] != nums[j] \
                            and abs(nums[i] - nums[j]) == k \
                            and (nums[i], nums[j]) not in valid_pairs:
                        valid_pairs.add((nums[i], nums[j]))
                        valid_pairs.add((nums[j], nums[i]))
                        valid_pair_count += 1
        # print(valid_pairs)
        return valid_pair_count


# assert basic test cases to show output as expected
assert Solution.find_pairs(nums=[3, 1, 4, 1, 5], k=2) == 2
assert Solution.find_pairs(nums=[1, 2, 3, 4, 5], k=1) == 4
assert Solution.find_pairs(nums=[1, 3, 1, 5, 4], k=0) == 1
assert Solution.find_pairs(nums=[1, 2, 4, 4, 3, 3, 0, 9, 2, 3], k=3) == 2
assert Solution.find_pairs(nums=[-1, -2, -3], k=1) == 2
"""
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2

Input: nums = [-1,-2,-3], k = 1
Output: 2
"""
