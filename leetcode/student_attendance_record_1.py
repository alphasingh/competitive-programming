"""
https://leetcode.com/problems/student-attendance-record-i/
"""


class Solution:
    @staticmethod
    def checkRecord(s: str) -> bool:
        return ('LLL' not in s) and s.count('A') < 2


assert Solution.checkRecord(s="PPALLP") is True
assert Solution.checkRecord(s="PPALLL") is False

"""
Example 1:
Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences 
and was never late 3 or more consecutive days.

Example 2:
Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, 
so is not eligible for the award.
"""

"""
Hint:
If the temperature is say, 70 today, 
then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. 
We could remember when all of them occur next.
"""
