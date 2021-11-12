"""
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
"""


class Solution:
    @staticmethod
    def isPrefixOfWord(sentence: str, searchWord: str) -> int:
        found_at = -1
        search_word_size = len(searchWord)
        for index, word in enumerate(sentence.split()):
            if searchWord == word[:search_word_size]:
                found_at = index + 1
                break
        return found_at


assert Solution.isPrefixOfWord(sentence="i love eating burger", searchWord="burg") == 4
"""
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
"""
assert Solution.isPrefixOfWord(sentence="this problem is an easy problem", searchWord="pro") == 2
"""
Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, 
but we return 2 as it's the minimal index.
"""
assert Solution.isPrefixOfWord(sentence="i am tired", searchWord="you") == -1
"""
Explanation: "you" is not a prefix of any word in the sentence.
"""
assert Solution.isPrefixOfWord(sentence="i use triple pillow", searchWord="pill") == 4
assert Solution.isPrefixOfWord(sentence="hello from the other side", searchWord="they") == -1
