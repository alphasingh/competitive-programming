"""
800
https://codeforces.com/problemset/problem/71/A
"""


class Solution:
    @staticmethod
    def shortenWord(word: str) -> str:
        length = len(word)
        if length > 10:
            word = word[0] + str(length - 2) + word[-1]
        return word


assert Solution.shortenWord("word") == "word"
assert Solution.shortenWord("localization") == "l10n"
assert Solution.shortenWord("internationalization") == "i18n"
assert Solution.shortenWord("pneumonoultramicroscopicsilicovolcanoconiosis") == "p43s"

for TC in range(int(input())):
    print(Solution.shortenWord(input()))

"""
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
-----------------------------------
word
l10n
i18n
p43s
"""
