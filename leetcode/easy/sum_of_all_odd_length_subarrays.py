"""
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
"""


class Solution:
    @staticmethod
    def sumOddLengthSubarrays(arr: [int]) -> int:
        total_odd_sum = 0
        size_of_array = len(arr)
        for size_of_sub_array in range(1, size_of_array + 1, 2):  # odd steps
            for start in range(size_of_array - size_of_sub_array + 1):
                total_odd_sum += sum(arr[start:start + size_of_sub_array])
        return total_odd_sum


assert Solution.sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3]) == 58
assert Solution.sumOddLengthSubarrays(arr=[1, 2]) == 3
assert Solution.sumOddLengthSubarrays(arr=[10, 11, 12]) == 66

"""
Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:
Input: arr = [10,11,12]
Output: 66
"""
