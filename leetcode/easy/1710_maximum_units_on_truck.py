"""
https://leetcode.com/problems/maximum-units-on-a-truck/
"""


class Solution:
    @staticmethod
    def maximumUnits(boxTypes: [[int]], truckSize: int) -> int:
        maximum_units = truckSize + len(boxTypes)
        return maximum_units


assert Solution.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4) == 8
"""
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
"""
assert Solution.maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10) == 91
