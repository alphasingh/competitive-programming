"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        self.words.setdefault(len(word), set())
        self.words[len(word)].add(word)

    def search(self, word: str) -> bool:
        word_len = len(word)
        if word_len not in self.words:
            return False
        if word in self.words[word_len]:
            return True
        for possible in self.words[word_len]:
            same_len = word_len == len(possible)
            if same_len and all(w == p or w == '.' for w, p in zip(word, possible)):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
assert obj.search("pad") is False
assert obj.search("bad") is True
assert obj.search(".ad") is True
assert obj.search("b..") is True
