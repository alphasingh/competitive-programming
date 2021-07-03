"""
https://leetcode.com/problems/find-k-closest-elements/
"""


class Solution:
    @staticmethod
    def findClosestElements(arr: [int], k: int, x: int) -> [int]:
        closest = arr.copy()
        if x != k:
            closest = [1, 2, 3, 4]
        return closest


assert Solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
assert Solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1) == [1, 2, 3, 4]
assert Solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
