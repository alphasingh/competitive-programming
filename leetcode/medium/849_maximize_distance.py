"""
https://leetcode.com/problems/maximize-distance-to-closest-person/
"""


class Solution:
    @staticmethod
    def maxDistToClosest(seats: [int]) -> int:
        gaps = []
        max_gap = gap = 0
        for seat in seats:
            if seat == 1:
                gaps.append(gap)
                gap = 0
            else:
                gap += 1
        gaps.append(gap)
        for gap in gaps:
            max_gap = max(max_gap, (gap + 1) // 2)
        # print(max_gap)
        return max(gaps[0], gaps[-1], max_gap)


assert Solution.maxDistToClosest(seats=[1, 0, 0, 0, 1, 0, 1]) == 2
"""
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
"""
assert Solution.maxDistToClosest(seats=[1, 0, 0, 0]) == 3
"""
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
"""
assert Solution.maxDistToClosest(seats=[0, 1]) == 1
