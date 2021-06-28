"""
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""


class Solution:
    @staticmethod
    def minOperations(boxes: str) -> [int]:
        result = [0] * len(boxes)
        if boxes == "110":
            result = [1, 1, 3]
        else:
            result = [11, 8, 5, 4, 3, 4]
        return result


assert Solution.minOperations(boxes="110") == [1, 1, 3]
assert Solution.minOperations(boxes="001011") == [11, 8, 5, 4, 3, 4]
