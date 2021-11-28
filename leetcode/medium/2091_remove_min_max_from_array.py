"""
https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
"""


class Solution:
    @staticmethod
    def minimumDeletions(nums: [int]) -> int:
        minimum = min(nums)
        maximum = max(nums)
        min_index = nums.index(minimum)
        max_index = nums.index(maximum)
        total = len(nums)
        left1 = min(max_index, min_index) + 1
        left2 = max(max_index, min_index) + 1
        right1 = total - left2 + 1
        right2 = total - left1 + 1
        # print(left1, left2, right1, right2)
        return min(left2, right2, left1 + right1)


assert Solution.minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]) == 5
"""
Explanation: 
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum 
by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.
"""
assert Solution.minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5]) == 3
"""
Explanation: 
The minimum element in the array is nums[1], which is -4.
The maximum element in the array is nums[2], which is 19.
We can remove both the minimum and maximum by removing 3 elements from the front.
This results in only 3 deletions, which is the minimum number possible.
"""
assert Solution.minimumDeletions([101]) == 1
"""
Explanation:  
There is only one element in the array, 
which makes it both the minimum and maximum element.
We can remove it with 1 deletion.
"""
