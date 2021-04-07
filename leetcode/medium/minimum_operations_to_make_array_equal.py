"""
https://leetcode.com/problems/minimum-operations-to-make-array-equal/
"""


class Solution:
    @staticmethod
    def minOperations(n: int) -> int:
        operations = 0
        if n & 1:  # n is odd
            n //= 2  # make pairs for each operation
            operations = n * (n + 1)  # sum of n even numbers
        else:  # n is even
            n //= 2  # make pairs for each operation
            operations = n * n  # sum of n odd numbers
        return operations


assert Solution.minOperations(3) == 2
"""
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
"""
assert Solution.minOperations(6) == 9
