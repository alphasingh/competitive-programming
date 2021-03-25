"""
https://leetcode.com/problems/advantage-shuffle/
"""


class Solution:

    @staticmethod
    def advantageCount(A: [int], B: [int]) -> [int]:
        index_b = {b: list() for b in B}
        permutation_a = A.copy()
        for index, b in enumerate(B):
            index_b[b].append(index)
        pointer_b = end_pointer_a = len(B) - 1  # same size of A and B
        start_pointer_a = 0
        sorted_b = sorted(B)
        sorted_a = sorted(A)
        while pointer_b >= 0:
            index = index_b[sorted_b[pointer_b]].pop()
            if sorted_a[end_pointer_a] > sorted_b[pointer_b]:
                permutation_a[index] = sorted_a[end_pointer_a]
                end_pointer_a -= 1
            else:
                permutation_a[index] = sorted_a[start_pointer_a]
                start_pointer_a += 1
            pointer_b -= 1
        # print(permutation_a)
        return permutation_a


assert Solution.advantageCount(A=[2, 7, 11, 15], B=[1, 10, 4, 11]) == [2, 11, 7, 15]
assert Solution.advantageCount(A=[12, 24, 8, 32], B=[13, 25, 32, 11]) == [24, 32, 8, 12]
