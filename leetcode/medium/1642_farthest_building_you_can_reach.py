"""
https://leetcode.com/problems/furthest-building-you-can-reach/
"""

import bisect


class Solution:

    @staticmethod
    def furthestBuilding_binarySearch(H, bricks, L):
        def isReach(k):
            to_climb = [y - x for y, x in zip(H[1:k + 1], H[:k + 1]) if y - x > 0]
            return len(to_climb) <= L or sum(sorted(to_climb)[::-1][L:]) <= bricks

        H += [float("inf")]
        beg, end = 0, len(H) - 1
        while beg + 1 < end:
            mid = (beg + end) // 2
            if isReach(mid):
                beg = mid
            else:
                end = mid
        return beg

    @staticmethod
    def furthestBuilding(heights: [int], bricks: int, ladders: int) -> int:
        farthest_building = 0
        # print(heights)
        jumps = []
        while farthest_building < len(heights) - 1:
            # print(jumps)
            height_difference = heights[farthest_building + 1] - heights[farthest_building]
            # print(height_difference, 'L:', ladders, 'B:', bricks)
            if height_difference > 0:  # next building is taller
                bisect.insort_right(jumps, height_difference)
            # print(jumps, jumps[:-ladders])
            bricks_needed = sum(jumps[:-ladders]) if ladders else sum(jumps)
            # print(bricks_needed)
            if bricks_needed <= bricks:
                farthest_building += 1
            else:
                break
        # print(farthest_building)
        return farthest_building


assert Solution.furthestBuilding(heights=[8, 18, 6, 11, 7, 22, 24, 7, 23], bricks=10, ladders=2) == 7
assert Solution.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2) == 7
assert Solution.furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0) == 3
assert Solution.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1) == 4
"""
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
"""
assert Solution.furthestBuilding(heights=[3, 19, 4, 14, 2, 7, 3, 18, 20], bricks=10, ladders=2) == 6
assert Solution.furthestBuilding(heights=[4, 7, 15, 3, 8, 4, 19, 21, 4, 7], bricks=10, ladders=2) == 8
assert Solution.furthestBuilding(heights=[6, 16, 4, 9, 5, 20, 22, 5, 8], bricks=10, ladders=2) == 8
assert Solution.furthestBuilding(heights=[1, 2], bricks=0, ladders=0) == 0
