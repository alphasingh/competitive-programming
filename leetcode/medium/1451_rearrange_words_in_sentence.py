"""
https://leetcode.com/problems/rearrange-words-in-a-sentence/
"""


class Solution:
    @staticmethod
    def arrangeWords(text: str) -> str:
        words = text.split()
        result = []
        hm = {}
        for word in words:
            l = len(word)
            if l not in hm:
                hm[l] = []
            hm[l].append(word)
        # print(hm)
        for key in sorted(hm.keys()):
            # print(hm[key])
            result += hm[key]
        output = " ".join(result).capitalize()
        return output


assert Solution.arrangeWords("Leetcode is cool") == "Is cool leetcode"
"""
Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter.
"""
assert Solution.arrangeWords("Keep calm and code on") == "On and keep calm code"
"""
Explanation: Output is ordered as follows:
"On" 2 letters.
"and" 3 letters.
"keep" 4 letters in case of tie order by position in original text.
"calm" 4 letters.
"code" 4 letters.
"""
assert Solution.arrangeWords("To be or not to be") == "To be or to be not"
