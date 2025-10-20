"""
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
"""
from typing import List


class Solution:
    @staticmethod
    def finalValueAfterOperations(operations: List[str]) -> int:
        X = 0
        for op in operations:
            if "+" in op:
                X += 1
            else:
                X -= 1
        return X


assert Solution.finalValueAfterOperations(["--X","X++","X++"]) == 1
assert Solution.finalValueAfterOperations(["++X","++X","X++"]) == 3
assert Solution.finalValueAfterOperations(["X++","++X","--X","X--"]) == 0
