"""
https://leetcode.com/problems/short-encoding-of-words/
"""


class Solution:
    @staticmethod
    def minimumLengthEncoding(words: [str]) -> int:
        parents = []

        # sort by length?
        # largest will always be the parent because word has to end at #
        words = [(word[::-1], len(word)) for word in words]
        words.sort(key=lambda x: x[1])
        # print(words)

        while words:
            word, size = words.pop()
            parent_found = False
            for p, l in parents:
                if p[:size] == word:
                    parent_found = True
                    break
            if not parent_found:
                parents.append((word, size))
            # print(words, parents)

        length = sum(len(parent[0]) for parent in parents) + len(parents)
        return length


assert Solution.minimumLengthEncoding(words=["time", "me", "bell"]) == 10
"""
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
"""
assert Solution.minimumLengthEncoding(words=["t"]) == 2
"""
Explanation: A valid encoding would be s = "t#" and indices = [0].
"""
