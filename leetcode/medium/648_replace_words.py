"""
https://leetcode.com/problems/replace-words/
"""


class Solution:
    @staticmethod
    def replaceWords(dictionary: [str], sentence: str) -> str:
        dictionary.sort(key=lambda item: (len(item), item))
        replaced_sentence = sentence.split()
        words = len(replaced_sentence)
        for i in range(words):
            replacement = replaced_sentence[i]
            for key in dictionary:
                if key == replacement[:len(key)]:
                    replacement = key
                    break
            replaced_sentence[i] = replacement
        return " ".join(replaced_sentence)


sample_output = "the cat was rat by the bat"
assert Solution.replaceWords(dictionary=["cat", "bat", "rat"],
                             sentence="the cattle was rattled by the battery") == sample_output
sample_output = "a a b c"
assert Solution.replaceWords(dictionary=["a", "b", "c"],
                             sentence="aadsfasf absbs bbab cadsfafs") == sample_output
sample_output = "a a a a a a a a bbb baba a"
assert Solution.replaceWords(dictionary=["a", "aa", "aaa", "aaaa"],
                             sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa") == sample_output
sample_output = "the cat was rat by the bat"
assert Solution.replaceWords(dictionary=["catt", "cat", "bat", "rat"],
                             sentence="the cattle was rattled by the battery") == sample_output
sample_output = "it is ab that this solution is ac"
assert Solution.replaceWords(dictionary=["ac", "ab"],
                             sentence="it is abnormal that this solution is accepted") == sample_output
