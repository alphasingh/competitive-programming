"""
1288. Remove Covered Intervals
https://leetcode.com/problems/remove-covered-intervals/
"""


class Solution:
    @staticmethod
    def remove_covered_intervals(intervals: [[int]]) -> int:
        super_intervals = 0  # intervals that can hold(include) other smaller(inclusive) intervals
        max_end_so_far = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))  # x[0] is interval start and x[1] is interval end
        for interval_start, interval_end in intervals:
            if interval_end > max_end_so_far:
                super_intervals += 1
                max_end_so_far = interval_end
        return super_intervals


assert Solution.remove_covered_intervals([[1, 4], [3, 6], [2, 8]]) == 2
assert (Solution.remove_covered_intervals([[1, 4], [2, 3]])) == 1
assert (Solution.remove_covered_intervals([[0, 10], [5, 12]])) == 2
assert (Solution.remove_covered_intervals([[3, 10], [4, 10], [5, 11]])) == 2
assert (Solution.remove_covered_intervals([[1, 2], [1, 4], [3, 4]])) == 1
"""
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Input: intervals = [[1,4],[2,3]]
Output: 1

Input: intervals = [[0,10],[5,12]]
Output: 2

Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2

Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1
"""
