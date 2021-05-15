"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"""


class Solution:
    @staticmethod
    def numberOfSteps(num: int) -> int:  # log num
        steps = 0
        while num:
            if num % 2 == 0:  # even
                num //= 2
            else:
                num -= 1
            steps += 1
        # print(steps)
        return steps


assert Solution.numberOfSteps(14) == 6
"""
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
"""
assert Solution.numberOfSteps(8) == 4
"""
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
"""
assert Solution.numberOfSteps(26) == 7
assert Solution.numberOfSteps(1000000) == 26
