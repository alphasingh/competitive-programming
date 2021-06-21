"""
https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True


trie = Trie()
trie.insert("word")
assert trie.search("word") is True
assert trie.startsWith("prefix") is False
assert trie.startsWith("w") is True
assert trie.startsWith("wo") is True
assert trie.startsWith("rd") is False

trie.insert("apple")
assert trie.search("apple") is True
assert trie.search("app") is False
assert trie.startsWith("app") is True
trie.insert("app")
assert trie.search("app") is True
