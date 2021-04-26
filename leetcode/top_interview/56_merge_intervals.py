"""
https://leetcode.com/problems/merge-intervals/
"""


class Solution:

    @staticmethod
    def merge(intervals: [[int]]) -> [[int]]:
        intervals.sort(key=lambda x: (x[1], -x[0]), reverse=True)  # sort by end times
        # print(intervals)
        for i in range(len(intervals) - 1):
            if intervals[i][0] < intervals[i + 1][0]:
                intervals[i + 1] = intervals[i]
            if intervals[i][0] <= intervals[i + 1][1]:
                intervals[i + 1][1] = intervals[i][1]
                intervals[i] = intervals[i + 1]
        # print(intervals)
        merged = dict()
        for interval in intervals:
            merged.setdefault(interval[1], 100000)
            merged[interval[1]] = min(merged[interval[1]], interval[0])
        # print(merged)
        return [[merged[key], key] for key in merged]


intervals_input = [[1, 4], [0, 2], [3, 5]]
assert sorted(Solution.merge(intervals_input), key=lambda x: x[0]) == [[0, 5]]

intervals_input = [[16, 18], [15, 18], [1, 3], [17, 18], [18, 18], [2, 6], [8, 10]]
assert sorted(Solution.merge(intervals_input), key=lambda x: x[0]) == [[1, 6], [8, 10], [15, 18]]

intervals_input = [[1, 3], [2, 6], [8, 10], [15, 18]]
assert sorted(Solution.merge(intervals_input), key=lambda x: x[0]) == [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

assert Solution.merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
