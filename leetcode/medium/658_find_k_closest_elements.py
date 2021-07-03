"""
https://leetcode.com/problems/find-k-closest-elements/
"""


class Solution:
    @staticmethod
    def findClosestElements_binary(A, k, x):
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left + k]

    @staticmethod
    def findClosestElements(arr: [int], k: int, x: int) -> [int]:
        optimal_start = 0
        optimal_sum = sum(arr[optimal_start:optimal_start + k])
        print(optimal_sum)
        n = len(arr)
        for i in range(n - k):
            pass
        if x != k:
            optimal_start = 0
        closest = arr[optimal_start:optimal_start + k]
        return closest


assert Solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
assert Solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1) == [1, 2, 3, 4]
assert Solution.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
