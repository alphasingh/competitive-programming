"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""

from collections import Counter


class Solution:
    LIMIT = 1_000_000

    def minDeletions(self, s: str) -> int:
        frequencies = sorted(Counter(s).values(), reverse=True)
        # print(frequencies)
        frequencies_set = set(frequencies)
        deletions = 0
        current = self.LIMIT
        for frequency in frequencies:
            if frequency == current:
                new_frequency = frequency
                while new_frequency > 0 and new_frequency in frequencies_set:
                    new_frequency -= 1
                current_deletions = frequency - new_frequency
                frequencies_set.add(new_frequency)
                # print('=', current, ' d:', current_deletions)
                deletions += current_deletions
            else:
                current = frequency
        return deletions


solution = Solution()
assert solution.minDeletions("aaaaabbbbbccccccccnmjuuttyy") == 7
assert solution.minDeletions("ceabaacb") == 2
assert solution.minDeletions("aab") == 0
assert solution.minDeletions("aaabbbcc") == 2
