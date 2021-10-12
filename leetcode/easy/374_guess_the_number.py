"""
https://leetcode.com/problems/guess-number-higher-or-lower/
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    @staticmethod
    def guessNumber(n: int) -> int:
        left = 1
        right = 2147483647
        # apply binary search to guess number
        while left <= right:
            mid = (left + right) // 2
            guessed = mid  # call guess(mid)
            if guessed == 0:  # correct guess
                return mid
            elif guessed == 1:  # go higher
                left = mid + 1
            else:  # go lower
                right = mid - 1
        return -1

# simple binary search based on given guess API
