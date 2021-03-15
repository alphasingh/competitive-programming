"""
https://leetcode.com/problems/daily-temperatures/
"""


class Solution:
    @staticmethod
    def dailyTemperatures(temperatures: [int]) -> [int]:  # brute force
        length_of_temperatures = len(temperatures)
        for today in range(length_of_temperatures):
            for higher in range(today + 1, length_of_temperatures):
                if temperatures[higher] > temperatures[today]:
                    temperatures[today] = higher - today
                    break
            else:
                temperatures[today] = 0
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
