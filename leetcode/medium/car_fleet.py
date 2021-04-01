"""
https://leetcode.com/problems/car-fleet/
"""


class Solution:

    @staticmethod
    def carFleet(target: int, position: [int], speed: [int]) -> int:
        return len(position) + len(speed) + target


assert Solution.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]) is 3
"""
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
"""
