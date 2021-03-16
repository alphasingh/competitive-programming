"""
https://leetcode.com/problems/daily-temperatures/
"""

import bisect


class Solution:
    MIN = 30
    MAX = 100

    @staticmethod
    def getPossibleTemperatures() -> dict:
        possible_temperatures = dict()  # map
        for temperature in range(Solution.MIN, Solution.MAX + 1):
            possible_temperatures[temperature] = list()
        return possible_temperatures

    @staticmethod
    def dailyTemperatures(temperatures: [int]) -> [int]:
        possible_temperatures = Solution.getPossibleTemperatures()
        for day, temperature_of_day in enumerate(temperatures):
            possible_temperatures[temperature_of_day].append(day)
        for day, temperature_of_day in enumerate(temperatures):
            higher = 1e10
            for possible_temperature in range(temperature_of_day + 1, Solution.MAX + 1):
                index = bisect.bisect(possible_temperatures[possible_temperature], day)
                if index < len(possible_temperatures[possible_temperature]):
                    higher = min(higher, possible_temperatures[possible_temperature][index])
            if higher < 1e10:
                temperatures[day] = higher - day
            else:
                temperatures[day] = 0
        return temperatures


input_1 = [73, 74, 75, 71, 69, 72, 76, 73]
output_1 = [1, 1, 4, 2, 1, 1, 0, 0]
assert Solution.dailyTemperatures(temperatures=input_1) == output_1

"""
Example 1:
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
"""

"""
Hint:
If the temperature is say, 70 today, 
then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. 
We could remember when all of them occur next.
"""
