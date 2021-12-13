"""
https://leetcode.com/problems/consecutive-characters/
"""


class Solution:
    @staticmethod
    def maxPower(s: str) -> int:
        count = 0
        max_count = 0
        last = s[0]
        for current in s:
            if current == last:
                count += 1
            else:
                last = current
                max_count = max(max_count, count)
                count = 1
        # print(count)
        max_count = max(max_count, count)
        return max_count


assert Solution.maxPower("leetcode") == 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
assert Solution.maxPower("abbcccddddeeeeedcba") == 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
assert Solution.maxPower("triplepillooooow") == 5
assert Solution.maxPower("hooraaaaaaaaaaay") == 11
assert Solution.maxPower("tourist") == 1
assert Solution.maxPower("effeegggeeee")
