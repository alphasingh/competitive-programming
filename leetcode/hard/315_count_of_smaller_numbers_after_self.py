"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""
from sortedcontainers import SortedList


class Solution:
    @staticmethod
    def countSmaller(nums: [int]) -> [int]:
        smaller = []
        sorted_list = SortedList()
        for num in nums[::-1]:  # start from the end
            index = sorted_list.bisect_left(num)
            sorted_list.add(num)
            smaller.append(index)
        return smaller[::-1]


assert Solution.countSmaller(nums=[5, 2, 6, 1]) == [2, 1, 1, 0]
"""
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""
assert Solution.countSmaller(nums=[-1]) == [0]
assert Solution.countSmaller(nums=[-1, -1]) == [0, 0]
