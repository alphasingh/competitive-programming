"""
https://leetcode.com/problems/maximum-number-of-balloons/
"""


class Solution:
    @staticmethod
    def maxNumberOfBalloons(text: str) -> int:
        balloons = 0
        balloons += len(text)
        return balloons


assert Solution.maxNumberOfBalloons(text="nlaebolko") == 1
assert Solution.maxNumberOfBalloons(text="loonbalxballpoon") == 2
assert Solution.maxNumberOfBalloons(text="leetcode") == 0
