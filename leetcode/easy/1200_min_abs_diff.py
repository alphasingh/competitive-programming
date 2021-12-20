"""
https://leetcode.com/problems/minimum-absolute-difference/
"""


class Solution:
    @staticmethod
    def minimumAbsDifference(arr: [int]) -> [[int]]:
        n = len(arr)
        diff = {}
        arr.sort()
        for i in range(n - 1):
            d = arr[i + 1] - arr[i]
            if d not in diff:
                diff[d] = []
            diff[d].append([arr[i], arr[i + 1]])
        return diff[min(diff.keys())]


assert Solution.minimumAbsDifference([4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]]
"""
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
"""
assert Solution.minimumAbsDifference([1, 3, 6, 10, 15]) == [[1, 3]]
assert Solution.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]) == [[-14, -10], [19, 23], [23, 27]]
