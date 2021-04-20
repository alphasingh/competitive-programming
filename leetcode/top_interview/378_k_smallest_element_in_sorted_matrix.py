"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""


class Solution:

    @staticmethod
    def kthSmallest(matrix: [[int]], k: int) -> int:
        n = len(matrix)
        flat_list = []
        for row in range(n):
            for column in range(n):
                flat_list.append(matrix[row][column])
        flat_list.sort()
        kth_smallest = flat_list[k - 1]
        return kth_smallest


assert Solution.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8) == 13
"""
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
"""
assert Solution.kthSmallest(matrix=[[-5]], k=1) == -5
