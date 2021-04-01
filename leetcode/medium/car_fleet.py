"""
https://leetcode.com/problems/car-fleet/
"""


class Solution:

    @staticmethod
    def carFleet(target: int, position: [int], speed: [int]) -> int:
        time_to_target = [float((target - p) / s) for p, s in sorted(zip(position, speed), reverse=True)]
        slowest = 0
        fleets = 0
        for time in time_to_target:
            if time > slowest:
                slowest = time
                fleets += 1
        return fleets


assert Solution.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]) is 3
"""
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
"""
