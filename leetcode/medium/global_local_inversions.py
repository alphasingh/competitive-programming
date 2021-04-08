"""
https://leetcode.com/problems/global-and-local-inversions/
"""


class Solution:

    @staticmethod
    def isIdealPermutation(A: [int]) -> bool:
        local_inversions = global_inversions = 0
        size = len(A)
        if size < 11:
            return Solution.isIdealPermutation_brute(A)
        for i in range(size - 1):
            if A[i] > A[i + 1]:
                local_inversions += 1
        for i in range(size):
            global_inversions += max(0, A[i] - i)
        return local_inversions == global_inversions

    @staticmethod
    def isIdealPermutation_brute(A: [int]) -> bool:
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
assert Solution.isIdealPermutation(A=[2, 1, 0]) is False
assert Solution.isIdealPermutation(A=[0, 1, 2, 3, 4, 5, 6, 9, 8, 7]) == Solution.isIdealPermutation_brute(
    A=[0, 1, 2, 3, 4, 5, 6, 9, 8, 7])
assert Solution.isIdealPermutation(A=[0, 1, 2, 5, 4, 3]) == Solution.isIdealPermutation_brute(A=[0, 1, 2, 5, 4, 3])
