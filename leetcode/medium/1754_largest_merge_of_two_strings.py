"""
https://leetcode.com/problems/largest-merge-of-two-strings/
"""


class Solution:
    @staticmethod
    def largestMerge(word1: str, word2: str) -> str:
        length_word1 = len(word1)
        length_word2 = len(word2)
        pointer1 = pointer2 = 0  # start both from left
        merged = []
        while pointer1 < length_word1 or pointer2 < length_word2:
            w = '#'
            if pointer1 < length_word1 and pointer2 < length_word2:  # both exist, so compare
                if word1[pointer1] > word2[pointer2]:
                    w = word1[pointer1]
                    pointer1 += 1
                elif word1[pointer1] < word2[pointer2]:
                    w = word2[pointer2]
                    pointer2 += 1
                else:
                    if word1[pointer1:] >= word2[pointer2:]:
                        w = word1[pointer1]
                        pointer1 += 1
                    else:
                        w = word2[pointer2]
                        pointer2 += 1
            elif pointer1 < length_word1:  # only word1 exists
                w = word1[pointer1]
                pointer1 += 1
            elif pointer2 < length_word2:  # only word2 exists
                w = word2[pointer2]
                pointer2 += 1
            merged.append(w)
            # print(pointer1, pointer2)
        # print(merged)
        return "".join(merged)


assert Solution.largestMerge(word1="cabaa", word2="bcaaa") == "cbcabaaaaa"
"""
Explanation: One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.
"""
assert Solution.largestMerge(word1="abcabc", word2="abdcaba") == "abdcabcabcaba"
largest_merge = "qqqqqqqqqqqqqqqqqeqqqeqeqqeeqqqeeqqeeqqqqqeq"
assert Solution.largestMerge("qqqqqqqqqeqeqqeeqqq", "qqqqqqqqeqqqeeqqeeqqqqqeq") == largest_merge
