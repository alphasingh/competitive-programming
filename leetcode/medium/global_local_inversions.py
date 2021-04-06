"""
https://leetcode.com/problems/global-and-local-inversions/
"""


class Solution:

    @staticmethod
    def isIdealPermutation(A: [int]) -> bool:
        local_inversions = global_inversions = 0
        size = len(A)
        for i in range(size):
            for j in range(i + 1, size):
                if A[i] > A[j]:
                    global_inversions += 1
        for i in range(size - 1):
            if A[i] > A[i + 1]:
                local_inversions += 1
        return local_inversions == global_inversions


assert Solution.isIdealPermutation(A=[1, 0, 2]) is True
# Explanation: There is 1 global inversion, and 1 local inversion.
assert Solution.isIdealPermutation(A=[1, 2, 0]) is False
# Explanation: There are 2 global inversions, and 1 local inversion.
