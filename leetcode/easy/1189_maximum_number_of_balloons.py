"""
https://leetcode.com/problems/maximum-number-of-balloons/
"""


class Solution:
    @staticmethod
    def maxNumberOfBalloons(text: str) -> int:
        f = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for character in text:
            if character in f:
                f[character] += 1
        # print(f)
        balloons = min(f['b'], f['a'], f['l'] // 2, f['o'] // 2, f['n'])
        return balloons


assert Solution.maxNumberOfBalloons(text="nlaebolko") == 1
assert Solution.maxNumberOfBalloons(text="loonbalxballpoon") == 2
assert Solution.maxNumberOfBalloons(text="leetcode") == 0
