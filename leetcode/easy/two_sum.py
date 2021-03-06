"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

import bisect


class Solution:
    @staticmethod
    def twoSum(numbers: [int], target: int) -> [int]:
        numbers_length = len(numbers)
        for first_index in range(numbers_length):
            second = target - numbers[first_index]
            second_index = bisect.bisect_right(numbers, second) - 1
            if second == numbers[second_index]:
                numbers[0] = first_index + 1
                numbers[1] = second_index + 1
                break
        return numbers[0:2]


assert Solution.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
assert Solution.twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
assert Solution.twoSum(numbers=[-1, 0], target=-1) == [1, 2]
assert Solution.twoSum(numbers=[5, 25, 75], target=100) == [2, 3]
assert Solution.twoSum(numbers=[0, 0, 3, 4], target=0) == [1, 2]

"""
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
"""

"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).
"""
