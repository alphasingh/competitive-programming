"""
https://leetcode.com/problems/merge-intervals/
"""


class Solution:

    @staticmethod
    def merge(intervals: [[int]]) -> [[int]]:
        merged = list(set(intervals))
        return merged


assert Solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
assert Solution.merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
