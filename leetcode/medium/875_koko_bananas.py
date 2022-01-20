"""
https://leetcode.com/problems/koko-eating-bananas/
"""

import math


class Solution:
    @staticmethod
    def minEatingSpeed(piles: [int], h: int) -> int:
        total = sum(piles)
        left = total // h
        k = right = total

        def is_possible(per_hour):
            if per_hour == 0:
                return False
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / per_hour)
            return hours <= h

        while left <= right:
            m = (left + right) // 2
            if is_possible(m):
                k = min(k, m)
                right = m - 1
            else:
                left = m + 1
        return k


assert Solution.minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4
assert Solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30
assert Solution.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23

"""
[30,11,23,4,20]
100000
[30,11,23,4,20]
88
[30,11,23,4,20]
8
[30,11,23,4,20]
9
[30,11,23,4,20]
13
[30,11,23,4,20]
16
[312884470]
968709470
"""
