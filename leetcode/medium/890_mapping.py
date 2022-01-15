"""
https://leetcode.com/problems/find-and-replace-pattern/
"""


class Solution:
    @staticmethod
    def findAndReplacePattern(words: [str], pattern: str) -> [str]:
        match = []
        # print(pc)
        n = len(pattern)
        for word in words:
            pm, wm = dict(), dict()
            matches = True
            for i in range(n):
                if pattern[i] not in pm and word[i] not in wm:
                    pm[pattern[i]] = word[i]
                    wm[word[i]] = pattern[i]
                if pattern[i] not in pm or word[i] not in wm or pm[pattern[i]] != word[i] or wm[word[i]] != pattern[i]:
                    matches = False
                    break
            if matches:
                match.append(word)
        return match


assert Solution.findAndReplacePattern(words=["abc",
                                             "deq",
                                             "mee",
                                             "aqq",
                                             "dkd",
                                             "ccc"],
                                      pattern="abb") == ["mee", "aqq"]
"""
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, 
since a and b map to the same letter.
"""
assert Solution.findAndReplacePattern(words=["a",
                                             "b",
                                             "c"],
                                      pattern="a") == ["a", "b", "c"]
