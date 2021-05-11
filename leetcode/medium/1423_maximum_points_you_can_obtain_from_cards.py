"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""


class Solution:

    @staticmethod
    def maxScore(cardPoints: [int], k: int) -> int:
        length = len(cardPoints)
        max_score = current_score = sum(cardPoints[:k])
        for slider in range(1, k + 1):
            current_score -= cardPoints[k - slider] - cardPoints[length - slider]
            max_score = max(max_score, current_score)
        return max_score


assert Solution.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3) == 12
"""
Explanation: After the first step, your score will always be 1. 
However, choosing the rightmost card first will maximize your total score.
The optimal strategy is to take the three cards on the right, 
giving a final score of 1 + 6 + 5 = 12.
"""
assert Solution.maxScore(cardPoints=[2, 2, 2], k=2) == 4
"""
Explanation: Regardless of which two cards you take, 
your score will always be 4.
"""
assert Solution.maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7) == 55
"""
Explanation: You have to take all the cards. 
Your score is the sum of points of all cards.
"""
assert Solution.maxScore(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3) == 202
assert Solution.maxScore(cardPoints=[1, 1000, 1], k=1) == 1
"""
Explanation: You cannot take the card in the middle. 
Your best score is 1. 
"""
