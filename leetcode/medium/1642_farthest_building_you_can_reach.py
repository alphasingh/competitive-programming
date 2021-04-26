"""
https://leetcode.com/problems/furthest-building-you-can-reach/
"""


class Solution:

    @staticmethod
    def furthestBuilding(heights: [int], bricks: int, ladders: int) -> int:
        farthest_building = len(heights) + bricks + ladders
        return farthest_building


assert Solution.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1) == 4
"""
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
"""
assert Solution.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2) == 7
assert Solution.furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0) == 3
