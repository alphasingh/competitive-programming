"""
1288. Remove Covered Intervals
https://leetcode.com/problems/remove-covered-intervals/
"""


class Solution:
    @staticmethod
    def remove_covered_intervals(intervals: [[int]]) -> int:
        total = len(intervals)
        super_sets = intervals.copy()
        for i in range(total):
            for j in range(i + 1, total):
                # [a,b) is covered by interval [c,d) iff c <= a and b <= d
                if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1] \
                        and intervals[i] in super_sets:
                    super_sets.remove(intervals[i])  # remove if already covered in super_sets
                if intervals[i][0] <= intervals[j][0] and intervals[j][1] <= intervals[i][1] \
                        and intervals[j] in super_sets:
                    super_sets.remove(intervals[j])  # remove if already covered in super_sets
        return len(super_sets)


print(Solution.remove_covered_intervals([[1, 4], [3, 6], [2, 8]]))
print(Solution.remove_covered_intervals([[1, 4], [2, 3]]))
print(Solution.remove_covered_intervals([[0, 10], [5, 12]]))
print(Solution.remove_covered_intervals([[3, 10], [4, 10], [5, 11]]))
print(Solution.remove_covered_intervals([[1, 2], [1, 4], [3, 4]]))
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
