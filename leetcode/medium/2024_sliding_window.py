"""
https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
"""


class Solution:
    @staticmethod
    def max_consecutive_answers(answer_key: str, k: int) -> int:
        # sliding window with max delta of 0 and 1 being k
        start = end = 0
        n = len(answer_key)
        trues = false = 0
        max_consecutive = 1
        while start <= end < n:
            if answer_key[end] == 'T':
                trues += 1
            else:
                false += 1
            changes = min(trues, false)
            # print(answerKey[start:end+1], k, changes)
            # bring start towards end until changes <= k
            while changes > k:
                if answer_key[start] == 'T':
                    trues -= 1
                else:
                    false -= 1
                changes = min(trues, false)
                start += 1
            max_consecutive = max(max_consecutive, end - start + 1)
            # print(answerKey[start:end+1], k, changes)
            end += 1
        return max_consecutive


assert Solution.max_consecutive_answers(answer_key="TTFF", k=2) == 4
"""
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
"""
assert Solution.max_consecutive_answers(answer_key="TFFT", k=1) == 3
"""
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
"""
assert Solution.max_consecutive_answers("TTFTTFTT", k=1) == 5
"""
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.
"""
