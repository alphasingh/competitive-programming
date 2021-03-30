"""
https://leetcode.com/problems/count-good-triplets/
"""


class Solution:
    @staticmethod
    def countGoodTriplets(arr: [int], a: int, b: int, c: int) -> int:
        len_arr = len(arr)
        count = 0
        for i in range(len_arr):
            for j in range(i + 1, len_arr):
                for k in range(j + 1, len_arr):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count


assert Solution.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3) is 4
assert Solution.countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1) is 0
